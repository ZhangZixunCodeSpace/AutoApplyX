import asyncio
import os
import uuid
from pathlib import Path

import uvicorn
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse

# 创建工作目录 workspace，如果不存在则创建
WORKSPACE_DIR = Path("workspace")
WORKSPACE_DIR.mkdir(exist_ok=True)

app = FastAPI()

# 开启 CORS 支持，允许前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议限制具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 模拟的 Agent Flow 函数
async def run_agent_flow(prompt: str, resume_path: str) -> str:
    """
    模拟根据 prompt 和 resume_path 处理任务，返回 Markdown 结果。
    真实情况中，这里将调用你的 AutoApplyAgent 以及相应的 Flow。
    """
    # 检查文件是否存在
    if not os.path.exists(resume_path):
        raise HTTPException(status_code=404, detail="Resume file not found")

    # 这里模拟读取部分文件内容（真实情况可能解析 PDF 文件）
    with open(resume_path, "rb") as f:
        file_content = f.read()

    # 模拟生成 Markdown 内容，这里仅简单拼接 prompt 和部分文件内容
    markdown_result = (
        "# Job Application Summary\n\n"
        f"**Prompt:** {prompt}\n\n"
        "The resume has been processed successfully.\n\n"
        "*(This is a simulated markdown result.)*"
    )
    return markdown_result


@app.post("/apply")
async def apply_job(resume: UploadFile = File(...), prompt: str = Form(...)):
    """
    接收前端上传的 resume 文件和 prompt 文本，并调用 Agent Flow 进行处理。
    1. 将 PDF 文件保存到 workspace 目录中。
    2. 调用 run_agent_flow 函数，传入 prompt 和文件路径。
    3. 返回生成的 Markdown 结果。
    """
    # 保存上传的 PDF 文件到 workspace 目录
    file_extension = os.path.splitext(resume.filename)[1]
    # 为避免文件名冲突，使用 UUID 生成唯一文件名
    file_name = f"resume_{str(uuid.uuid4())}{file_extension}"
    file_path = WORKSPACE_DIR / file_name

    try:
        with open(file_path, "wb") as f:
            content = await resume.read()
            f.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

    # 调用 Agent Flow 进行处理
    try:
        result = await run_agent_flow(prompt, str(file_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent flow error: {str(e)}")

    # 返回处理结果（Markdown 格式文本）
    return JSONResponse({"result": result})


@app.get("/")
async def index():
    """
    提供一个简单的 HTML 页面用于测试上传功能
    """
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>AutoApplyX</title>
      </head>
      <body>
        <h1>AutoApplyX Test Page</h1>
        <form action="/apply" method="post" enctype="multipart/form-data">
          <label for="resume">Upload Resume (PDF):</label><br>
          <input type="file" name="resume" id="resume" required><br><br>
          <label for="prompt">Prompt:</label><br>
          <textarea name="prompt" id="prompt" rows="4" cols="50" placeholder="Enter your prompt here" required></textarea><br><br>
          <button type="submit">Submit</button>
        </form>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/download_markdown")
async def download_markdown(file_name: str):
    """
    通过指定文件名下载 Markdown 文件（如果需要保存 Markdown 文件后展示）
    """
    file_path = WORKSPACE_DIR / file_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename=file_name)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
