# book_recomentation
Here's a `README.md` file for your **AI Book Recommendation Assistant** using Cohere:

---

```markdown
# 📚 AI Book Recommendation Assistant using Cohere

This Python script is a simple command-line tool that uses **Cohere's large language model** to generate personalized book recommendations based on books you’ve liked in the past.

---

## 📌 Features

- Accepts user input of favorite books
- Uses Cohere’s `command-r-plus` model to find and recommend 5 similar books
- Each recommendation includes a short explanation
- Lightweight and easy to run from the terminal

---

## 🧪 Example

```

Enter the names of books you liked: The Alchemist, Atomic Habits

📚 Recommended Books:

1. Man's Search for Meaning – A deeply introspective book on purpose and resilience, similar to the reflective tone of *The Alchemist*.
2. Deep Work by Cal Newport – A great follow-up for fans of *Atomic Habits*, focusing on focused productivity.
3. The Four Agreements – Philosophical and spiritual like *The Alchemist*, it explores personal freedom.
4. The Power of Now – Another spiritual guide that pairs well with the mindset explored in *The Alchemist*.
5. Tiny Habits by BJ Fogg – A practical book on behavioral change, expanding on ideas found in *Atomic Habits*.

````

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-book-recommender.git
cd ai-book-recommender
````

### 2. Install Dependencies

```bash
pip install cohere
```

### 3. Add Your Cohere API Key

Replace your key in the script:

```python
co = cohere.Client('your_api_key_here')
```

💡 **Best Practice**: Use environment variables for security:

```python
import os
co = cohere.Client(os.getenv("COHERE_API_KEY"))
```

---

## 💻 Run the App

```bash
python book_recommender.py
```

Enter your list of favorite books when prompted.

---

## 🔒 Security Note

**Never commit your API key** to public repositories. Use `.env` files or environment variables for safer deployments.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤖 Powered By

* [Cohere](https://cohere.com)

```

---

Would you like a version of this app with a GUI using Streamlit or Tkinter?
```
