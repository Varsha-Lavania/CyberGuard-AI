import pandas as pd
import matplotlib.pyplot as plt
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# -------------------------------
# CLEAN TEXT
# -------------------------------
def clean_text(text):
    text = str(text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"http\S+|www\S+", " link ", text)
    text = re.sub(r"\d+", " number ", text)
    text = re.sub(r"[^a-zA-Z0-9\s$!]", " ", text)
    return text.lower()


# -------------------------------
# EXTRACT BODY
# -------------------------------
def extract_body(text):
    text = str(text)

    text = re.sub(r"(Subject:.*\n)", "", text, flags=re.IGNORECASE)
    text = re.sub(r"(From:.*\n)", "", text, flags=re.IGNORECASE)
    text = re.sub(r"(To:.*\n)", "", text, flags=re.IGNORECASE)

    text = re.split(r"(-{2,}|From:)", text)[0]

    return text.strip()


# -------------------------------
# RULE CHECK
# -------------------------------
def rule_based_check(message):
    suspicious_words = [
        "win", "free", "urgent", "click", "offer",
        "password", "otp", "bank", "lottery", "prize"
    ]

    return [word for word in suspicious_words if word in message.lower()]


# -------------------------------
# LOAD DATA
# -------------------------------
print("Loading dataset...")
data = pd.read_csv("spam.csv", encoding="latin-1", on_bad_lines='skip')

data["clean_text"] = data["text"].astype(str).apply(clean_text)
data["label_num"] = data["label"].map({"ham": 0, "spam": 1})


# -------------------------------
# MODEL TRAINING
# -------------------------------
vectorizer = TfidfVectorizer(stop_words="english", max_features=2000)

X = vectorizer.fit_transform(data["clean_text"])
y = data["label_num"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))


# -------------------------------
# INPUT SYSTEM
# -------------------------------
print("\nPaste your email or message below.")
print("Type 'END' on a new line when you are done.\n")

lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    lines.append(line)

msg = "\n".join(lines)

if not msg.strip():
    print("Empty message. Exiting.")
    exit()


# -------------------------------
# PROCESSING
# -------------------------------
body = extract_body(msg)
cleaned = clean_text(body)

if not cleaned.strip():
    print("Message too short after cleaning. Exiting.")
    exit()

detected_words = rule_based_check(body)
score = len(detected_words)

num_links = len(re.findall(r"http\S+|www\S+", msg))
num_numbers = len(re.findall(r"\d+", msg))
num_caps = sum(1 for word in msg.split() if word.isupper())

msg_data = vectorizer.transform([cleaned])
prob = model.predict_proba(msg_data)[0][1]


# -------------------------------
# DECISION
# -------------------------------
if prob > 0.7 or score >= 2 or num_links > 1 or num_caps > 3:
    verdict = "Spam (High Risk)"
elif prob > 0.4 or score == 1:
    verdict = "Suspicious"
else:
    verdict = "Safe"


# -------------------------------
# OUTPUT
# -------------------------------
print("\nMessage Analysis Report")
print("----------------------------------")
print("Extracted Body:\n", body)
print("----------------------------------")
print("Spam Probability:", round(prob * 100, 2), "%")
print("Suspicious Keywords:", detected_words if detected_words else "None")
print("Links Found:", num_links)
print("Numbers Found:", num_numbers)
print("Capital Words:", num_caps)
print("Final Verdict:", verdict)

# Risk level
if verdict == "Spam (High Risk)":
    print("Risk Level: HIGH")
elif verdict == "Suspicious":
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")

print("----------------------------------")


# -------------------------------
# FINAL GRAPH
# -------------------------------
words = cleaned.split()
total_words = len(words)
normal_words = max(total_words - score, 0)

summary_data = {
    "Spam Probability (%)": prob * 100,
    "Suspicious Words": score,
    "Normal Words": normal_words
}

plt.figure()
plt.bar(summary_data.keys(), summary_data.values())
plt.title("Message Analysis Summary")
plt.ylabel("Value")
plt.show()