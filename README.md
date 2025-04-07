# AutoApplyX

**AutoApplyX** is an AI-powered job application automation agent built on top of the full OpenManus framework. It automates your job search by parsing and optimizing your resume, searching for targeted positions (e.g., frontend developer roles on CTgoodjobs), automatically submitting applications, generating a Markdown summary of your applications, and optionally importing that summary into Notion for efficient tracking.

> **Note:** This project is forked from [OpenManus](https://github.com/mannaandpoem/OpenManus). The original OpenManus documentation is preserved in [OPENMANUS_README.md](OPENMANUS_README.md) for reference.

---

## Features

- **Built on OpenManus:** Leverages OpenManus’s complete multi-agent, multi-tool, and flow orchestration capabilities.
- **Resume Parsing & Optimization:** Automatically extracts key information from your resume and optimizes it for ATS systems.
- **Automated Job Applications:** Searches for suitable positions on CTgoodjobs, fills out application forms, and submits applications automatically.
- **Markdown Summary Generation:** Compiles a summary of all applications in Markdown format.
- **Notion Integration:** Optionally uploads the generated Markdown summary to your Notion workspace.
- **Modular & Extensible:** Easily add or modify tools and flows based on your evolving requirements.

---

## Project Structure

```
AutoApplyX/
├── app/
│   ├── agent/              # Custom agents (e.g., AutoApplyAgent) extending OpenManus's ToolCallAgent
│   ├── flow/               # Custom flows (e.g., AutoApplyFlow, FlowFactory) for orchestrating multi-step tasks
│   ├── tool/               # Custom tools (BrowserUseTool, FileSaver, ResumeParserTool, NotionTool, etc.)
│   ├── config.py           # Configuration settings (workspace paths, API keys, etc.)
│   ├── logger.py           # Logging utilities for consistent log output
│   └── __init__.py
├── frontend/               # Front-end code (UI for file uploads, status display, etc.)
├── run_flow.py             # Entry script to run the AutoApplyX flow
├── requirements.txt        # Python dependencies (including OpenManus and other required libraries)
├── OPENMANUS_README.md     # Original OpenManus documentation and configuration details
├── README.md               # This file – AutoApplyX project documentation
└── .gitignore              # Files and directories to ignore (e.g., __pycache__, venv, node_modules)
```

---

## Installation

### 1. Fork & Clone the Repository

1. **Fork the OpenManus Repository:**  
   Visit [OpenManus](https://github.com/mannaandpoem/OpenManus) and click the **Fork** button to fork it into your account. Rename your fork to **AutoApplyX** (or update its description) to reflect your custom project.

2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/yourusername/AutoApplyX.git
   cd AutoApplyX
   ```
   *Note: Cloning creates a directory named “AutoApplyX” – you need to run `cd AutoApplyX` to change into that directory before working on the project.*

### 2. Set Up the Environment

1. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies:**
   Make sure that `requirements.txt` includes OpenManus and other required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running from the Command Line

To run the AutoApplyX flow, execute:
```bash
python run_flow.py
```
Example prompt:
```
I have uploaded my resume at 'workspace/resume.pdf'. Please search for 'frontend developer' positions on CTgoodjobs, apply with my optimized resume, generate a markdown summary of the applications, and upload the summary to Notion.
```
The system will then sequentially perform the following:
- Parse and optimize your resume.
- Search for relevant job postings.
- Automatically submit applications.
- Generate a Markdown summary of your applications.
- Optionally integrate the summary with Notion.
The final result will be displayed in your terminal.

### API for Front-End Integration

A sample FastAPI endpoint is provided for integration with a front-end UI. Example (`app_server.py`):

```python
from fastapi import FastAPI, UploadFile, File
import uvicorn
from run_flow import run_flow

app = FastAPI()

@app.post("/apply")
async def apply_job(resume: UploadFile = File(...)):
    # Save the uploaded resume to the workspace directory
    with open("workspace/resume.pdf", "wb") as f:
        f.write(await resume.read())
    # Execute the AutoApplyX flow
    result = await run_flow()
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Front-end developers can use this endpoint to upload resumes and retrieve the application summary.

---

## Branch Workflow & Team Collaboration

To streamline team development, we recommend the following branch strategy:

1. **Backend Branch (`backend`):**  
   - Develop and modify all back-end components (Agent, Flow, and Tool modules).
   - Example:
     ```bash
     git checkout -b backend
     # Develop backend code...
     git add .
     git commit -m "Develop backend: Add AutoApplyAgent and AutoApplyFlow"
     git push origin backend
     ```

2. **Frontend Branch (`frontend`):**  
   - Develop UI and API integration in the `frontend/` directory.
   - Example:
     ```bash
     git checkout main
     git checkout -b frontend
     # Develop front-end code...
     git add .
     git commit -m "Develop frontend: Create UI for file upload and application status display"
     git push origin frontend
     ```

3. **Feature Integration Branch (`feature/autoapplyx`):**  
   - Merge both backend and frontend branches into this integration branch, test the overall functionality, and then merge into the main branch.
   - Example:
     ```bash
     git checkout main
     git checkout -b feature/autoapplyx
     git merge backend
     git merge frontend
     # Resolve conflicts if any, then:
     git push origin feature/autoapplyx
     ```

After thorough testing, merge the feature branch into the main branch.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository and create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
2. Commit your changes with clear commit messages.
3. Push your branch and open a pull request for review.

For front-end contributions, please coordinate with the backend team to ensure API consistency.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or support, please open an issue in this repository or contact the project maintainers.

---

**AutoApplyX** leverages the power of the complete OpenManus framework to provide an innovative solution for automating job applications. This project streamlines the job application process and frees you to focus on what matters most. Enjoy and happy coding!

