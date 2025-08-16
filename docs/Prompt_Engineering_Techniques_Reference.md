# Prompt Engineering Techniques Reference

## Techniques Used in Role-Based Smart Document Helper

### 1. **System Role Definition**
Each prompt begins with a clear system instruction that defines the AI's role:

```python
"SYSTEM: You are a knowledgeable teacher who explains concepts clearly..."
"SYSTEM: You are an expert reviewer providing critical analysis..."
```

### 2. **Behavioral Instructions**
Specific guidelines for how each role should behave:

```python
# Teacher Role
"When answering:
- Break down complex ideas into simple terms
- Use analogies and examples where helpful
- Encourage understanding with a patient, educational tone"

# Expert Reviewer Role
"When answering:
- Provide thorough, analytical responses
- Evaluate claims critically
- Maintain objectivity and professionalism"
```

### 3. **Context Framing**
Different labels for the same input to reinforce the role:

- Teacher: "STUDENT'S QUESTION:"
- Expert: "QUESTION FOR REVIEW:"
- Technical Writer: "TECHNICAL QUERY:"

### 4. **Output Format Control**
Role-specific formatting instructions:

```python
# Technical Writer
"- Use structured, precise language
- Include bullet points or numbered lists where appropriate"

# Friendly Assistant
"- Use a warm, conversational tone
- Make the information accessible"
```

### 5. **Tone and Style Markers**
Unique response markers for each role:

- "TEACHER'S RESPONSE:"
- "EXPERT ANALYSIS:"
- "TECHNICAL RESPONSE:"

### 6. **Task-Specific Adaptations**
Each role has variations for different tasks:

- **QA Prompts**: Focus on answering style
- **Summary Prompts**: Focus on organization and emphasis
- **Translation Prompts**: Focus on register and formality

### 7. **Constraint Instructions**
Clear boundaries for each role:

```python
# Legal Advisor
"Important: You are not providing actual legal advice, only information based on the document."
```

## Best Practices Demonstrated

### ✅ **Clarity First**
- Each role has clear, unambiguous instructions
- No conflicting directives

### ✅ **Consistency**
- Role traits maintained across all task types
- Unified terminology within each role

### ✅ **Specificity**
- Concrete examples of desired behavior
- Precise formatting requirements

### ✅ **Flexibility**
- Roles adapt to different tasks while maintaining identity
- Balance between structure and natural language

### ✅ **User Context**
- Consider the audience for each role
- Appropriate complexity levels

## Example: Complete Teacher Role QA Prompt

```python
"""SYSTEM: You are a knowledgeable teacher who explains concepts clearly. 
Use the following context to answer the question. 
If the answer is not found in the context, state that you cannot answer based on the provided information.

When answering:
- Break down complex ideas into simple terms
- Use analogies and examples where helpful
- Encourage understanding with a patient, educational tone
- If the concept is difficult, provide step-by-step explanations

CONTEXT:
{context}

STUDENT'S QUESTION: {query}

TEACHER'S RESPONSE:"""
```

## Key Insights

1. **Role Consistency > Complexity**: Simple, consistent role definitions work better than overly complex ones
2. **Examples Help**: Showing the model how to behave is more effective than just telling
3. **Structure Matters**: Clear prompt structure helps maintain role boundaries
4. **Context is King**: How you present information affects how the model processes it
5. **Less Can Be More**: Concise, focused instructions often outperform lengthy ones

## Prompt Engineering Principles Applied

1. **Be Specific**: Vague instructions lead to inconsistent outputs
2. **Use Positive Instructions**: Tell the model what to do, not just what to avoid
3. **Provide Structure**: Clear sections and formatting improve response quality
4. **Test Iteratively**: Each role required multiple refinements
5. **Consider Token Economy**: Balance detail with available token space

---

This reference guide demonstrates how thoughtful prompt engineering can create distinct, useful AI behaviors without any model modifications.