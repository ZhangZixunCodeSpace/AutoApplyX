import { useState, useRef, useEffect } from 'react';
import { Input, Button, Upload, Typography, Spin, Divider, Empty, message } from 'antd';
import { SendOutlined, FileOutlined, DeleteOutlined, UserOutlined, RobotOutlined } from '@ant-design/icons';
import ReactMarkdown from 'react-markdown';

const { Title, Text } = Typography;
const { TextArea } = Input;

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [fileList, setFileList] = useState([]);
    const messageEndRef = useRef(null);

    // 自动滚动到最新消息
    useEffect(() => {
        messageEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    // 处理文件上传前检查
    const beforeUpload = (file) => {
        // 这里可以添加文件类型和大小的验证逻辑
        const isAccepted = file.type === 'application/pdf' || file.name.endsWith('.pdf');

        if (!isAccepted) {
            message.error('只支持上传 PDF 文件!');
            return Upload.LIST_IGNORE;
        }

        const isLt10M = file.size / 1024 / 1024 < 10;
        if (!isLt10M) {
            message.error('文件必须小于10MB!');
            return Upload.LIST_IGNORE;
        }

        return false; // 阻止自动上传
    };

    // 文件变更处理
    const handleFileChange = ({ fileList: newFileList }) => {
        setFileList(newFileList);
    };

    // 删除文件
    const handleFileRemove = (file) => {
        const index = fileList.indexOf(file);
        const newFileList = fileList.slice();
        newFileList.splice(index, 1);
        setFileList(newFileList);
    };

    // 发送消息和文件
    const handleSend = async () => {
        if ((!input.trim() && fileList.length === 0) || isLoading) return;

        const newMessage = {
            id: Date.now(),
            content: input,
            sender: 'user',
            files: fileList.map(file => file.name),
            timestamp: new Date().toISOString()
        };

        setMessages([...messages, newMessage]);
        setInput('');
        setIsLoading(true);

        try {
            // 创建FormData对象，用于发送文件和消息
            const formData = new FormData();
            formData.append('prompt', input);
            fileList.forEach(file => {
                formData.append('files', file.originFileObj);
            });

            // 发送到后端接口
            // 这里是示例代码，实际实现需根据后端接口调整
            // const response = await fetch('/api/chat', {
            //   method: 'POST',
            //   body: formData,
            // });

            // 模拟后端响应
            await new Promise(resolve => setTimeout(resolve, 1000));

            const agentResponse = {
                id: Date.now() + 1,
                content: "我已收到您的请求" + (input ? `: ${input}` : '') +
                    (fileList.length > 0 ? `，以及${fileList.length}个文件。` : '。') +
                    "作为AutoApplyX系统的AI助手，我可以帮您处理简历优化、自动申请工作等任务。请问有什么具体的需求吗？",
                sender: 'agent',
                timestamp: new Date().toISOString()
            };

            setMessages(messages => [...messages, agentResponse]);
            setFileList([]);
        } catch (error) {
            console.error('发送消息失败:', error);
            message.error('发送消息失败，请重试');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-full">
            {/* 聊天头部 */}
            <div className="flex-none p-4 border-b border-gray-200">
                <Title level={4} className="m-0">AutoApplyX AI 助手</Title>
                <Text type="secondary">基于 OpenManus 框架的智能求职辅助系统</Text>
            </div>

            {/* 聊天内容区域 */}
            <div className="flex-grow overflow-y-auto p-4 custom-scrollbar">
                {messages.length === 0 ? (
                    <div className="h-full flex items-center justify-center">
                        <Empty
                            description="开始与 AI 助手对话"
                            image={Empty.PRESENTED_IMAGE_SIMPLE}
                        />
                    </div>
                ) : (
                    messages.map((msg) => (
                        <div
                            key={msg.id}
                            className={`chat-message ${msg.sender === 'user' ? 'user-message' : 'agent-message'}`}
                        >
                            <div className="flex items-center gap-2 mb-1">
                                {msg.sender === 'user' ? (
                                    <UserOutlined className="text-blue-500" />
                                ) : (
                                    <RobotOutlined className="text-gray-500" />
                                )}
                                <Text strong>{msg.sender === 'user' ? '您' : 'AI 助手'}</Text>
                                <Text type="secondary" className="text-xs">
                                    {new Date(msg.timestamp).toLocaleTimeString()}
                                </Text>
                            </div>

                            <ReactMarkdown className="prose prose-sm max-w-none">
                                {msg.content}
                            </ReactMarkdown>

                            {msg.files && msg.files.length > 0 && (
                                <div className="mt-2">
                                    <Text type="secondary" className="text-xs">已上传文件:</Text>
                                    <div className="flex flex-wrap gap-2 mt-1">
                                        {msg.files.map((file, index) => (
                                            <div
                                                key={index}
                                                className="flex items-center gap-1 bg-gray-100 px-2 py-1 rounded-md text-xs"
                                            >
                                                <FileOutlined />
                                                <span>{file}</span>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}
                        </div>
                    ))
                )}
                <div ref={messageEndRef} />
            </div>

            {/* 输入区域 */}
            <div className="flex-none p-4 border-t border-gray-200">
                <div className="flex flex-col gap-2">
                    <TextArea
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        placeholder="输入您的请求..."
                        autoSize={{ minRows: 1, maxRows: 6 }}
                        onPressEnter={(e) => {
                            if (!e.shiftKey) {
                                e.preventDefault();
                                handleSend();
                            }
                        }}
                        disabled={isLoading}
                        className="rounded-md"
                    />

                    <div className="flex justify-between items-center input-actions">
                        <div className="flex items-center gap-2">
                            <Upload
                                beforeUpload={beforeUpload}
                                fileList={fileList}
                                onChange={handleFileChange}
                                onRemove={handleFileRemove}
                                multiple
                                showUploadList={false}
                            >
                                <Button
                                    icon={<FileOutlined />}
                                    className="flex items-center"
                                >
                                    上传文件
                                </Button>
                            </Upload>

                            {fileList.length > 0 && (
                                <Text type="secondary" className="text-xs">
                                    已选择 {fileList.length} 个文件
                                </Text>
                            )}
                        </div>

                        <Button
                            type="primary"
                            icon={<SendOutlined />}
                            onClick={handleSend}
                            loading={isLoading}
                            disabled={(!input.trim() && fileList.length === 0) || isLoading}
                            className="flex items-center"
                        >
                            发送
                        </Button>
                    </div>

                    {/* 显示选择的文件 */}
                    {fileList.length > 0 && (
                        <div className="flex flex-wrap gap-2 mt-2">
                            {fileList.map((file, index) => (
                                <div
                                    key={index}
                                    className="flex items-center gap-1 bg-gray-100 px-2 py-1 rounded-md text-xs"
                                >
                                    <FileOutlined />
                                    <span className="max-w-[150px] truncate">{file.name}</span>
                                    <DeleteOutlined
                                        className="text-red-500 cursor-pointer"
                                        onClick={() => handleFileRemove(file)}
                                    />
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Chat;
