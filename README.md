
# 🔐 Dottar - A Secure Git-Inspired Version Control System

Dottar is a lightweight, open-source version control system (VCS) built with Python. Inspired by Git, Dottar adds **security-first features** like encrypted commits, password-protected restore, and simplified file history management — all via an easy-to-use CLI.

> 🔧 Ideal for solo developers, students, and educational OS projects who want Git-like functionality with more privacy control.

---

## ✨ Features

- ✅ `init`, `add`, `commit`, `status`, `log` – Git-style commands
- 🔐 Optional Secure Mode (AES encryption + password)
- 🔄 `checkout` – restore any previous version securely
- 🧾 `diff` – view line-by-line changes between commits
- 📦 `clone` – locally copy a repository with full history
- 💻 Cross-platform CLI (Windows, macOS, Linux)
<!--- 🚀 Also available as a standalone `.exe` (no Python needed!)-->

---

## 📦 Download Dottar

### 🔹 For Developers (via Python)

```bash
git clone https://github.com/forkandflow/dottar.git
cd dottar
pip install .
```

Now use Dottar anywhere:

```bash
dottar init
```

---

Dottar for non python users as .exe will be comming soon.

---

## 🚀 How to Use

### 📁 Initialize a Dottar repo

```bash
dottar init
```

> 💡 You’ll be asked if you want to enable secure mode (set a master password).

---

### ➕ Add files

```bash
dottar add <filename>
```

---

### ✅ Commit files

```bash
dottar commit -m "Initial commit"
```

---

### 🔎 Check status

```bash
dottar status
```

---

### 🕘 View commit history

```bash
dottar log
```

---

### 🔁 Restore any commit

```bash
dottar checkout <commit_id>
```

> 🔐 Secure mode will ask for master password to decrypt blobs.

---

### 📄 View diff between commits

```bash
dottar diff <commit_id_1> <commit_id_2>
```

---

### 📥 Clone a repo locally

```bash
dottar clone <source_path> <target_path>
```

---

## 🔐 Secure Mode

- When enabled during `init`, files are encrypted during commits.
- You’ll be prompted for password during commit and restore.
- Uses `cryptography`’s AES-GCM encryption.

---

## 🧪 Project Structure

```
dottar/
├── dottar.py            ← Main CLI entry point
├── dottar_cli/          ← Command modules
│   ├── init.py, add.py, ...
│   └── utils/
├── requirements.txt     ← Dependencies
├── setup.py             ← Installable CLI via pip
├── README.md
```

---

## 🛠 Dependencies

- Python 3.7+
- [cryptography](https://pypi.org/project/cryptography/)

Install manually:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the MIT License © 2025 [Your Name]

---

## 🌐 Project Links

- 🔗 GitHub Repo: https://github.com/forkandflow/dottar
- 📘 Documentation: https://forkandflow.github.io/Dottar/
- 📥 Releases: https://forkandflow.github.io/Dottar/

---

## 🤝 Contribute

**Dottar is in active development and currently in public beta phase.**

We welcome all contributors to help improve and grow the project!

📌 Whether it's improving CLI design, fixing bugs, adding features, or writing docs — **your contributions matter**.

Please read the `CONTRIBUTING.md` (coming soon) and open a pull request or issue.

> ❤️ Let’s build Dottar together!

