import { useState } from 'react'
import { ConfigProvider } from 'antd'
import zhCN from 'antd/locale/zh_CN'
import Chat from './components/Chat'
import Sidebar from './components/Sidebar'
import './App.css'

function App() {
  return (
    <ConfigProvider locale={zhCN}>
      <div className="flex h-screen w-screen overflow-hidden bg-white absolute top-0 left-0 right-0 bottom-0">
        {/* 侧边栏 (固定宽度) */}
        <div className="w-[250px] h-full flex-shrink-0">
          <Sidebar />
        </div>

        {/* 聊天区域 */}
        <div className="flex-1 h-full">
          <Chat />
        </div>
      </div>
    </ConfigProvider>
  )
}

export default App
