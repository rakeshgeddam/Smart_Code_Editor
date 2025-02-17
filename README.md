# Smart_Code_Editor
Code editor powered by Vector Database to retrieve error support from historical logs 

## Overview
This project is a Python-based code editor built using `Tkinter` for the graphical user interface (GUI) and `Qdrant`, a vector database, for advanced code indexing and retrieval. The editor supports syntax highlighting, file management, and the ability to store and search code snippets using Qdrant.

![image](https://github.com/user-attachments/assets/2210ee4c-1bcf-45e7-8edd-ed3e5e32772d)



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

## License
This project is licensed under the MIT License.

