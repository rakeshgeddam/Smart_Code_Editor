# Smart_Code_Editor

**Code Editor Powered by Vector Database for Instant Error Support and Historical Log Retrieval**


## 🚀 Problem Statement

Modern developers waste significant time searching for solutions to repetitive errors. Traditional editors do not leverage historical log data for instant support.

**Smart_Code_Editor** bridges this gap by using a vector database (Qdrant) to store, retrieve, and suggest solutions to code errors from previous sessions—empowering developers to debug and learn faster. This project is a Python-based code editor built using `Tkinter` for the graphical user interface (GUI) and `Qdrant`, a vector database, for advanced code indexing and retrieval. The editor supports syntax highlighting, file management, and the ability to store and search code snippets using Qdrant.

***

![Architecture flow of Smart_Code_Editor: Editor, Vector DB, Retrieval, Suggestion.]
<img width="348" height="348" alt="image" src="https://github.com/user-attachments/assets/5c0b7add-2895-4bac-9951-082c014c34db" />

![Demo Screenshot]
![image](https://github.com/user-attachments/assets/2210ee4c-1bcf-45e7-8edd-ed3e5e32772d)

***


## 🌟 Key Features

- **Instant Error Retrieval:** Get contextual error support by searching historical logs using semantic similarity.
- **Vector Database Integration:** Uses Qdrant for scalable, fast log storage and nearest neighbor search.
- **Script Execution:** Run Python scripts directly; save outputs/errors to logs for future retrieval.
- **GUI Built with Tkinter:** Simple, intuitive interface for editing and troubleshooting.
- **Extensible Architecture:** Modular design for adding plugins and supporting multiple languages.
- **Open Source Collaboration:** Easy for other developers to contribute error datasets or feature ideas.

***

## 🖼️ Architecture Overview

1. **User edits code in GUI**
2. **Script execution triggers error logging**
3. **Error details are embedded and stored in Qdrant Vector DB**
4. **When a new error occurs, semantic search retrieves relevant solutions from the DB**
5. **Suggested solutions displayed in the editor**

*See architecture diagram above.*

***

## 💡 Use Case Scenario

**Imagine:** You hit a "TypeError" in your ML pipeline.
- Editor searches your previous logs for similar error messages.
- It retrieves a solution (ex: fixing data type in pandas DataFrame).
- You debug in seconds—no need to search StackOverflow manually.

***

## 🛠️ Technology Stack

- **Python 3**
- **Tkinter (GUI)**
- **Qdrant (Vector DB)**
- **OpenAI Embeddings (for semantic similarity)**
- **Docker (future roadmap)**

***

## 🎯 Value Proposition

- **Save debugging time:** Reduce error resolution by up to 30%
- **Learn from history:** Build your own knowledge-base as you code
- **Seamless workflow:** No context-switching between editor and support forums

***

## 🧗 Challenges Faced & Solutions

- **Efficient embedding storage:** Tuned Qdrant vectors for tens of thousands of logs.
- **Fast retrieval:** Used batch requests to optimize vector search latency.
- **GUI and backend communication:** Designed with separation of concerns for scalability.

***

## Features
- **Basic Code Editing**: Create, edit, save, and run Python scripts.
- **Syntax Highlighting**: Improve code readability.
- **Qdrant Integration**: Store and search code snippets using vector embeddings.
- **Execution Support**: Run Python scripts directly from the editor.


## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `tkinter` (comes with Python)
- `qdrant-client` for interacting with Qdrant
- `subprocess` for executing Python scripts
- `numpy` for handling vector embeddings (if required)

### Setup
1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd <project-directory>
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Application**
   ```sh
   python main.py
   ```

## Usage
### Code Editor
- Open the application and start coding in the editor.
- Save or run scripts directly from the interface.

### Qdrant Integration
- The project connects to a Qdrant instance to store and retrieve code snippets.
- Configure Qdrant connection settings in `config.py`.

### Running Scripts
- Click the "Run" button to execute scripts.
- Output is displayed within the application.

## Configuration
Modify `config.py` to customize:
- Qdrant server settings
- File save/load paths

## Future Enhancements
- Auto-completion using AI models
- Multi-file project support
- Dark mode theme

## Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## 👤 About Me

I developed Smart_Code_Editor to solve real developer pain points and deepen my expertise in information retrieval, scalable databases, and production-ready software systems.

If you’re interested in data engineering or intelligent developer tools, let’s connect!  
rakeshge@umich.edu | [LinkedIn](https://linkedin.com/in/rakeshgeddam)


