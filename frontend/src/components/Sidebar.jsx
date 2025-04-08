import { useState } from 'react';
import { Menu, Button, Typography, Divider, Badge } from 'antd';
import {
    PlusOutlined,
    MessageOutlined,
    HistoryOutlined,
    SettingOutlined,
    FileTextOutlined,
    UserOutlined
} from '@ant-design/icons';

const { Title, Text } = Typography;

const Sidebar = () => {
    const [selectedKey, setSelectedKey] = useState('new-chat');

    // 假设的历史聊天数据
    const chatHistory = [
        { id: 1, title: '前端开发工作申请', time: '2023-04-01', unread: 2 },
        { id: 2, title: '简历优化分析', time: '2023-03-28' },
        { id: 3, title: 'CTgoodjobs职位搜索', time: '2023-03-25' },
    ];

    return (
        <div className="sidebar flex flex-col h-full">
            {/* 侧边栏头部 */}
            <div className="p-4">
                <div className="flex items-center justify-between mb-2">
                    <Title level={4} className="m-0">AutoApplyX</Title>
                </div>
                <Text type="secondary" className="text-xs">AI 求职助手</Text>

                <Button
                    type="primary"
                    icon={<PlusOutlined />}
                    className="mt-4 w-full"
                    onClick={() => setSelectedKey('new-chat')}
                >
                    新建对话
                </Button>
            </div>

            <Divider className="my-1" />

            {/* 导航菜单 */}
            <div className="flex-grow overflow-y-auto custom-scrollbar">
                <Menu
                    mode="inline"
                    selectedKeys={[selectedKey]}
                    onSelect={({ key }) => setSelectedKey(key)}
                    className="border-r-0"
                >
                    <Menu.Item key="new-chat" icon={<MessageOutlined />}>
                        当前对话
                    </Menu.Item>

                    <Menu.SubMenu
                        key="history"
                        icon={<HistoryOutlined />}
                        title="历史记录"
                    >
                        {chatHistory.map(chat => (
                            <Menu.Item key={`chat-${chat.id}`} className="pl-8">
                                <div className="flex items-center justify-between">
                                    <div className="truncate max-w-[140px]">{chat.title}</div>
                                    {chat.unread && (
                                        <Badge count={chat.unread} size="small" />
                                    )}
                                </div>
                                <div className="text-xs text-gray-400">{chat.time}</div>
                            </Menu.Item>
                        ))}
                    </Menu.SubMenu>

                    <Menu.Item key="resume" icon={<FileTextOutlined />}>
                        我的简历
                    </Menu.Item>

                    <Menu.Item key="profile" icon={<UserOutlined />}>
                        个人资料
                    </Menu.Item>
                </Menu>
            </div>

            {/* 侧边栏底部 */}
            <div className="p-4 border-t border-gray-200">
                <Menu mode="inline" className="border-r-0">
                    <Menu.Item key="settings" icon={<SettingOutlined />}>
                        设置
                    </Menu.Item>
                </Menu>
            </div>
        </div>
    );
};

export default Sidebar;
