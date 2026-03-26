# CyberGuard AI – Intelligent Spam Detection System

CyberGuard AI is a machine learning-based spam detection system designed to identify and classify messages and emails as Safe, Suspicious, or Spam. The system combines Natural Language Processing (NLP) with rule-based analysis to provide accurate and practical results in real-world scenarios.

---

## Overview

With the increasing number of digital communications, spam messages and fraudulent emails have become a major cybersecurity concern. CyberGuard AI addresses this problem by analyzing the content of messages, extracting meaningful information, and applying both statistical and rule-based techniques to determine risk levels.

---

## Key Features

- Supports both short messages and full-length emails
- Automatically extracts the relevant body of emails
- Handles multiline input without errors
- Cleans and preprocesses text for better accuracy
- Uses TF-IDF vectorization for feature extraction
- Applies Naive Bayes machine learning model
- Includes rule-based keyword detection
- Detects links, numeric patterns, and excessive capitalization
- Generates a summarized analysis graph (single output per message)
- Provides clear classification:
  - Safe
  - Suspicious
  - Spam (High Risk)

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Regular Expressions (re)

---

## Dataset

This project uses a labeled dataset (`spam.csv`) for training and testing the model.

- Classes:
  - Ham (Safe messages)
  - Spam (Malicious or promotional messages)

Dataset source: Kaggle (Spam Detection Dataset)

---

## System Workflow

1. User inputs a message or email
2. System extracts the main content (ignores headers, greetings, signatures)
3. Text is cleaned and normalized
4. Feature extraction using TF-IDF
5. Machine learning prediction using Naive Bayes
6. Rule-based analysis checks for suspicious keywords and patterns
7. Final classification is generated
8. Optional summary graph is displayed

---

## Project Structure
```
CyberGuard-AI/
│
├── main.py # Main program file
├── spam.csv # Dataset used for training
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
└── report/
└── CyberGuard_Report.pdf

```


---

## Screenshots

### Input
<img width="1356" height="244" alt="image" src="https://github.com/user-attachments/assets/f3157364-88d1-4ef6-8369-9848c622e6e6" />


### Output
<img width="1368" height="324" alt="image" src="https://github.com/user-attachments/assets/eb20d97c-64cf-4f81-b01a-372e4ac1f537" />


### Graph
<img width="652" height="569" alt="image" src="https://github.com/user-attachments/assets/e8fcdc5d-aa6f-41fd-95ab-1a72771badd7" />


---

## Installation and Setup

1. Clone the repository:

git clone https://github.com/Varsha-Lavania/CyberGuard-AI

2. Navigate to the project folder:

cd CyberGuard-AI

3. Install dependencies:

pip install -r requirements.txt
 
4. Run the program:

python main.py


---

## Usage Instructions

- Paste the full message or email into the terminal
- Press Enter twice to submit
- View the analysis report
- Optionally choose to display the graph

---

## Model Details

- Vectorization: TF-IDF (Term Frequency-Inverse Document Frequency)
- Algorithm: Multinomial Naive Bayes
- Evaluation Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-Score

---

## Results

The model provides reliable spam detection by combining machine learning probability with heuristic rules. It is capable of identifying common spam patterns such as:

- Promotional keywords
- Phishing attempts
- Suspicious links
- Urgency-based language

---

## Advantages

- Simple and efficient implementation
- Works with real-world email formats
- Minimal computational requirements
- Easy to understand and extend

---

## Limitations

- Accuracy depends on dataset quality
- May not detect highly sophisticated spam
- Limited to text-based analysis (no attachments or images)

---

## Future Enhancements

- Web-based user interface
- Integration with email services
- Deep learning-based classification
- Real-time spam filtering system

---

## Conclusion

CyberGuard AI demonstrates how machine learning and rule-based logic can be effectively combined to detect spam messages and emails. The project highlights practical implementation of NLP techniques and provides a strong foundation for further cybersecurity applications.

---

## References

- Kaggle Spam Dataset
- Scikit-learn Documentation
- Python Official Documentation
- Cybersecurity Awareness Resources

---
