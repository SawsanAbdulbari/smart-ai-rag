# Smart Document Helper with Role-Based Prompting

## Project Overview

This project improves the Smart Document Helper RAG (Retrieval-Augmented Generation) system by implementing **Role-Based Prompting / Persona Simulation**. The improvement allows users to interact with documents through different AI personas, each providing unique perspectives and communication styles.

## Project Structure

```
D:\ai\hamk2ndyear\Prompt_Engineering_summer\
│
├── Smart_AI_Role_Prompting.ipynb   # Main implementation notebook
├── Role_Based_Prompting_Report.md           # Detailed project report
├── README.md                                 # This file
└── sample_outputs/                           # (Create this folder for saving example outputs)
```

## Features

### 🎭 Five Distinct AI Roles

1. **👩‍🏫 Teacher**
   - Explains concepts clearly with examples
   - Uses analogies and step-by-step explanations
   - Patient and educational approach

2. **🔍 Expert Reviewer**
   - Provides critical analysis
   - Evaluates claims objectively
   - Thorough and professional

3. **⚖️ Legal Advisor**
   - Uses formal, precise language
   - Includes appropriate disclaimers
   - Cautious interpretation

4. **💻 Technical Writer**
   - Structured documentation style
   - Clear technical terminology
   - Organized with sections and bullet points

5. **😊 Friendly Assistant**
   - Conversational and approachable
   - Makes complex ideas simple
   - Warm and encouraging tone

### Capabilities

- **Dynamic Prompt Templates**: Each role has custom prompts for Q&A, summarization, and translation
- **Role Information Display**: Visual indicators and descriptions for each role
- **Flexible Task Support**: All roles work across different task types
- **Improved User Experience**: Intuitive interface with role selection

## Installation and Setup

### Prerequisites

- Python 3.8+
- CUDA-capable GPU (recommended) or CPU
- Hugging Face account (for model access)

### Installation Steps

1. **Install required packages**:
   ```bash
   pip install faiss-cpu
   pip install gradio
   pip install pypdf
   pip install torch torchvision torchaudio
   pip install transformers
   pip install sentence-transformers
   pip install bitsandbytes  # For 4-bit quantization
   ```

2. **Authenticate with Hugging Face**:
   ```bash
   huggingface-cli login
   ```

3. **Run the notebook**:
   - Open `Smart_AI_Role_Prompting.ipynb` in Jupyter or Google Colab
   - Execute all cells in order
   - The Gradio interface will launch automatically

## Usage

1. **Upload a PDF document** using the file upload component
2. **Select an AI role** from the dropdown menu
3. **Choose a task**:
   - Ask a question
   - Summarize
   - Translate (to Finnish)
4. **Enter your query** (required for questions, optional for other tasks)
5. **Click Process** to get role-specific responses

## Technical Details

### Models Used
- **Embedding Model**: `all-MiniLM-L6-v2` (fast and efficient)
- **Language Model**: `google/gemma-2b-it` (2B parameter instruction-tuned model)
- **Vector Store**: FAISS for similarity search

### Key Components
- **Document Processing**: PDF text extraction and chunking
- **Semantic Search**: FAISS-based retrieval of relevant chunks
- **Role-Based Generation**: Dynamic prompt templates per role
- **4-bit Quantization**: Optional memory optimization for GPU

## Example Outputs

### Question: "What are the key findings?"

**Teacher Response**:
> "Let me break this down for you! Think of it like this..."

**Expert Reviewer Response**:
> "Upon critical examination of the findings, three aspects warrant attention..."

**Technical Writer Response**:
> "## Key Findings
> 1. Performance Metrics
>    - Metric A: 40% improvement
>    - Metric B: 2x throughput increase..."

## Future improvements

- [ ] Multi-role comparison view
- [ ] Custom role creation interface
- [ ] Role-specific conversation memory
- [ ] Export responses in different formats
- [ ] Support for more languages

## Troubleshooting

### Common Issues

1. **CUDA Out of Memory**:
   - Enable 4-bit quantization
   - Reduce chunk size
   - Use a smaller model

2. **Slow CPU Performance**:
   - Consider using Google Colab with GPU
   - Reduce max_new_tokens
   - Use smaller embedding model

3. **PDF Processing Errors**:
   - Ensure PDF contains extractable text
   - Check file permissions
   - Try re-saving the PDF

## Credits

- Base RAG implementation from HAMK AI course materials
- Improved with role-based prompting techniques
- Inspired by best practices from OpenAI, Anthropic, and Google prompt engineering guides

## License

This project is for educational purposes as part of the HAMK Prompt Engineering course.

---

For questions or improvements, please refer to the detailed report in `Role_Based_Prompting_Report.md`.