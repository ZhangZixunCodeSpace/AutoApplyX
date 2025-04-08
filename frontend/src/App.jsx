import { useState } from 'react'
import { ConfigProvider } from 'antd'
import zhCN from 'antd/locale/zh_CN'
import Chat from './components/Chat'
import Sidebar from './components/Sidebar'
import './App.css'

function App() {
  return (
    <ConfigProvider locale={zhCN}>
      <div className="flex h-screen overflow-hidden bg-white">
        {/* 侧边栏 (占屏幕宽度的 1/5) */}
        <div className="w-1/5 min-w-[250px] max-w-[300px]">
          <Sidebar />
        </div>

        {/* 聊天区域 (占屏幕宽度的 4/5) */}
        <div className="flex-1 flex flex-col">
          <Chat />
        </div>
      </div>
    </ConfigProvider>
  )
}

export default App
