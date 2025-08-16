# 🚀 Quick Start Guide

## Ultra-Enhanced Smart Document Helper

### 5-Minute Setup

#### 1. **Clone/Download the Project**
```bash
cd D:\ai\hamk2ndyear\Prompt_Engineering_summer
```

#### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

#### 3. **Login to Hugging Face**
```bash
huggingface-cli login
# Enter your token when prompted
```

#### 4. **Run the Application**
- Open `Ultra_Smart_AI_Multi_Strategy_RAG.ipynb` in Jupyter
- Run all cells (Cell → Run All)
- Wait for Gradio link to appear

### 🎯 Quick Usage Examples

#### Example 1: Simple Question
1. Upload any PDF document
2. Select **"Friendly Assistant"** role
3. Choose **"standard"** strategy
4. Ask: "What is this document about?"

#### Example 2: Technical Analysis
1. Same document
2. Select **"Expert Reviewer"** role
3. Choose **"chain_of_thought"** strategy
4. Ask: "What are the main limitations of this approach?"

#### Example 3: Educational Summary
1. Same document
2. Select **"Teacher"** role
3. Choose **"combined"** strategy
4. Enable **"Self-Consistency"**
5. Ask: "Explain the key concepts for a beginner"

### 🔥 Pro Tips

1. **For Best Results**:
   - Use "combined" strategy for important queries
   - Enable self-consistency for critical questions
   - Add custom examples for your specific domain

2. **For Faster Responses**:
   - Use "standard" strategy
   - Disable self-consistency
   - Keep queries focused

3. **For Learning**:
   - Try the same query with different roles
   - Compare strategies side-by-side
   - Edit prompts to see impact

### 📊 Strategy Selection Guide

| Your Need | Best Strategy | Best Role |
|-----------|--------------|-----------|
| Quick answer | Standard | Friendly Assistant |
| Detailed analysis | Chain-of-Thought | Expert Reviewer |
| Learning/Teaching | Combined | Teacher |
| Technical docs | Few-Shot | Technical Writer |
| Formal reports | Combined | Legal Advisor |

### 🆘 Troubleshooting

**"CUDA out of memory"**
→ Restart kernel, use CPU, or reduce tokens

**"Slow generation"**
→ Disable self-consistency, use simpler strategy

**"Poor results"**
→ Try different role/strategy combination

### 📚 Next Steps

1. Read the [full documentation](./Ultra_Enhanced_README.md)
2. Review the [technical report](./Ultra_Enhanced_Multi_Strategy_Report.md)
3. Experiment with [prompt engineering](./Prompt_Engineering_Techniques_Reference.md)
4. Create custom roles and strategies

---

**Need help?** Check the main README or report files for detailed information.

*Happy prompting! 🎉*