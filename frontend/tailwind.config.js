/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {},
    },
    // 防止与 Ant Design 冲突
    corePlugins: {
        preflight: false,
    },
    important: true, // 确保 Tailwind 样式优先级高于 Ant Design
}
