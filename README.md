# AutoApplyX

**AutoApplyX** is an AI-powered job application automation agent built on top of the full OpenManus framework. It extends OpenManus by adding functionality for automated resume parsing, ATS optimization, job application submission (e.g., on CTgoodjobs), Markdown summary generation, and Notion integration for tracking your job application progress.

> **Note:** This project is forked from [OpenManus](https://github.com/mannaandpoem/OpenManus). The original OpenManus documentation is preserved in [OPENMANUS_README.md](OPENMANUS_README.md) for reference.

---

## Features

- **Built on OpenManus:** Utilizes the complete multi-agent, multi-tool, and flow orchestration capabilities of OpenManus.
- **Resume Upload & Parsing:** Automatically extracts key details from your resume.
- **ATS Optimization & Automated Application:** Searches for suitable positions (e.g., frontend developer roles on CTgoodjobs), optimizes your resume for ATS, fills out application forms, and submits applications automatically.
- **Markdown Summary Generation:** Compiles a summary of all submitted applications in Markdown format.
- **Notion Integration:** Optionally uploads the generated Markdown summary to Notion for efficient tracking.
- **Modular & Extensible:** Easily add or modify tools and flows based on the OpenManus architecture.

---

## Project Structure

```
AutoApplyX/
├── app/
│   ├── agent/              # Custom agents (e.g., AutoApplyAgent)
│   ├── flow/               # Custom flows (e.g., AutoApplyFlow, FlowFactory)
│   ├── tool/               # Custom tools (BrowserUseTool, FileSaver, ResumeParserTool, NotionTool, etc.)
│   ├── config.py           # Configuration settings (workspace, API keys, etc.)
│   ├── logger.py           # Logging utilities
│   └── __init__.py
├── frontend/               # Front-end code (UI for file upload, job status display, etc.)
├── run_flow.py             # Entry script to run the AutoApplyX flow
├── requirements.txt        # Python dependencies (including OpenManus and others)
├── OPENMANUS_README.md     # Original OpenManus documentation
├── README.md               # This file – AutoApplyX project documentation
└── .gitignore              # Files and directories to ignore (e.g., __pycache__, venv, node_modules)
```

---

## Installation

### 1. Fork & Clone the Repository

1. **Fork the OpenManus Repository:**  
   Visit [OpenManus](https://github.com/mannaandpoem/OpenManus) and click the **Fork** button. Rename your fork to **AutoApplyX** (or add “AutoApplyX” in the description) for clarity.

2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/yourusername/AutoApplyX.git
   cd AutoApplyX
   ```

### 2. Set Up the Environment

1. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies:**
   Ensure `requirements.txt` includes OpenManus and other required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Command-Line Interface

To start the AutoApplyX flow from the command line, run:
```bash
python run_flow.py
```
For example, you might be prompted with:
```
I have uploaded my resume at 'workspace/resume.pdf'. 
Please search for 'frontend developer' positions on CTgoodjobs, apply with my optimized resume, generate a markdown summary of the applications, and upload the summary to Notion.
```
The system will sequentially perform resume parsing, job application submission, Markdown summary generation, and optionally push the summary to Notion.

### API for Front-End Integration

A sample FastAPI endpoint is provided (see `app_server.py` below) for front-end integration:
```python
from fastapi import FastAPI, UploadFile, File
import uvicorn
from run_flow import run_flow

app = FastAPI()

@app.post("/apply")
async def apply_job(resume: UploadFile = File(...)):
    # Save the uploaded resume to a designated path
    with open("workspace/resume.pdf", "wb") as f:
        f.write(await resume.read())
    # Run the AutoApplyX flow
    result = await run_flow()
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
Front-end developers can use this endpoint to upload resumes and receive the job application summary.

---

## Branch Workflow & Team Collaboration

For effective collaboration, we recommend the following Git workflow:

1. **Backend Development Branch:**  
   Create a branch named `backend` for developing and modifying the Agent, Flow, and tool-related code.

2. **Frontend Development Branch:**  
   Create a branch named `frontend` for developing the UI, file upload functionality, and API integration.

3. **Feature Integration Branch:**  
   Once both backend and frontend components are developed and tested, merge them into a common feature branch (e.g., `feature/autoapplyx`), and then merge that into the main branch.

Example commands:
```bash
# Create and push backend branch
git checkout -b backend
# ... develop backend code
git add .
git commit -m "Develop backend AutoApplyAgent and flow"
git push origin backend

# Create and push frontend branch
git checkout main
git checkout -b frontend
# ... develop frontend code in /frontend
git add .
git commit -m "Develop frontend UI and API integration"
git push origin frontend

# Create integration branch
git checkout main
git checkout -b feature/autoapplyx
git merge backend
git merge frontend
# Resolve any conflicts, then:
git push origin feature/autoapplyx
```
Once testing is complete, merge `feature/autoapplyx` into the main branch.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository and create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
2. Commit your changes with clear commit messages.
3. Push your branch to your fork and submit a pull request for review.

For front-end contributions, please coordinate with the back-end team to ensure API consistency.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or support, please open an issue in this repository or contact the project maintainers.

---

**AutoApplyX** leverages the complete OpenManus framework to deliver an innovative automated job application solution. Enjoy streamlining your job search and application process!

---

This README should serve as a comprehensive guide for both new developers and team members. It explains the project purpose, structure, installation, usage, and team workflow. Adjust any details to better match your project's specifics as needed.

Below is a refined sample README based on your input. You can use it as a starting point and adjust it as needed.

---

# AutoApplyX

**AutoApplyX** is an automated job application agent built on the OpenManus framework. Leveraging OpenManus’s comprehensive multi-agent, multi-tool, and multi-flow collaboration capabilities, AutoApplyX extends the original configuration and documentation by adding features such as automated resume parsing, ATS optimization, job application submission (using CTgoodjobs as an example), Markdown-based application record generation, and Notion integration.

> **Note:** This project is forked from [OpenManus](https://github.com/mannaandpoem/OpenManus). The original OpenManus documentation is preserved in the [OPENMANUS_README.md](OPENMANUS_README.md) file for reference.

---

## Project Overview

AutoApplyX automates the tedious parts of the job application process by:
- Parsing and optimizing your resume for ATS systems.
- Automatically searching and applying to targeted positions on platforms like CTgoodjobs.
- Generating a Markdown summary of your job applications.
- Optionally integrating with Notion to help you track your application progress.

---

## Project Structure

```
AutoApplyX/
├── app/
│   ├── agent/              # Custom agents (e.g., AutoApplyAgent)
│   ├── flow/               # Custom flows (e.g., AutoApplyFlow, FlowFactory)
│   ├── tool/               # Custom tools (e.g., BrowserUseTool, FileSaver, ResumeParserTool, NotionTool)
│   ├── config.py           # Configuration settings (workspace, API keys, etc.)
│   ├── logger.py           # Logging utilities
│   └── __init__.py
├── frontend/               # Front-end code for file upload, UI, etc.
├── run_flow.py             # Entry script to run the AutoApplyX flow
├── requirements.txt        # Python dependencies (including OpenManus and others)
├── OPENMANUS_README.md     # Original OpenManus documentation
├── README.md               # This file – AutoApplyX project documentation
└── .gitignore              # Files and directories to ignore (e.g., __pycache__, venv, node_modules)
```

---

## Installation

### 1. Fork & Clone the Repository

1. **Fork the OpenManus Repository:**  
   Visit [OpenManus](https://github.com/mannaandpoem/OpenManus) and click the **Fork** button to fork the repository to your GitHub account. Then, rename your fork to **AutoApplyX** (or update its description accordingly).

2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/yourusername/AutoApplyX.git
   cd AutoApplyX
   ```

### 2. Set Up the Environment

1. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies:**
   Make sure `requirements.txt` includes OpenManus and all necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Flow from the Command Line

Execute the following command to start the AutoApplyX flow:
```bash
python run_flow.py
```
For example, you might be prompted with:
```
I have uploaded my resume at 'workspace/resume.pdf'. 
Please search for 'frontend developer' positions on CTgoodjobs, apply with my optimized resume, generate a markdown summary of the applications, and upload the summary to Notion.
```
The system will sequentially parse the resume, perform job application submissions, generate a Markdown summary, and (if configured) integrate with Notion. The final result will be displayed in the terminal.

### API for Front-End Integration

A sample FastAPI endpoint is provided for front-end integration. Here’s an example (`app_server.py`):

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

Front-end developers can use this endpoint to upload a resume and receive the application result (e.g., the Markdown summary).

---

## Branch Workflow & Team Collaboration

To support effective team collaboration, we recommend the following Git branch strategy:

1. **Backend Branch:**  
   Create a branch named `backend` for developing and modifying the Agent, Flow, and tool-related backend code.
   ```bash
   git checkout -b backend
   ```
2. **Frontend Branch:**  
   Create a branch named `frontend` for developing the UI, file upload functionality, and API integration.
   ```bash
   git checkout main
   git checkout -b frontend
   ```
3. **Feature Integration Branch:**  
   Once both backend and frontend components are developed and tested, merge them into a feature branch (e.g., `feature/autoapplyx`), then merge that branch into the main branch.
   ```bash
   git checkout main
   git checkout -b feature/autoapplyx
   git merge backend
   git merge frontend
   # Resolve conflicts, commit, and then push:
   git push origin feature/autoapplyx
   ```

After testing the integration, merge the feature branch into the main branch.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository and create a new feature branch:
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

For questions or support, please open an issue in this repository or contact the project maintainers.

---

**AutoApplyX** leverages the full power of the OpenManus framework to provide an innovative solution for automating job applications. Enjoy streamlining your job search and improving your application efficiency!
