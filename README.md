# OctoFit Tracker - Build Applications with GitHub Copilot Agent Mode

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

[![GitHub Copilot](https://img.shields.io/badge/GitHub-Copilot-512a97?style=flat-square&logo=github)](https://github.com/features/copilot)
[![Django](https://img.shields.io/badge/Django-4.1.7-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react)](https://reactjs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0-47A248?style=flat-square&logo=mongodb)](https://www.mongodb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

> 🌍 **Available in:** [English](#english) | [Italiano](#italiano) | [Français](#français) | [Српски](#српски-serbian) | [Shqip](#shqip-albanian) | [हिन्दी](#हिन्दी-hindi)

---

## English

### 📚 Overview

**OctoFit Tracker** is a comprehensive fitness tracking application designed for educational purposes, specifically for Mergington High School. This project demonstrates how to build modern web applications using GitHub Copilot Agent Mode, combining cutting-edge AI assistance with proven development practices.

This repository serves as both a learning exercise and a real-world application example, showing developers how to leverage GitHub Copilot's autonomous capabilities to accelerate development across multiple technologies.

### 🎯 Project Purpose

This project was created to help students and developers:
- Learn to build full-stack web applications with AI assistance
- Master GitHub Copilot Agent Mode for autonomous development
- Understand modern web development stack (React + Django + MongoDB)
- Practice prompt engineering and AI-assisted coding
- Build real-world applications that solve actual problems

### ✨ Features

- **User Authentication & Profiles**: Secure user registration and management
- **Activity Logging & Tracking**: Track various fitness activities (running, walking, strength training)
- **Team Management**: Create and manage fitness teams
- **Competitive Leaderboard**: Gamified fitness competition with points and rankings
- **Personalized Workout Suggestions**: AI-powered recommendations based on user activity
- **Achievement System**: Badges and milestones to maintain engagement
- **Progress Dashboard**: Visual representation of fitness progress over time

### 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Frontend** | React.js | 18.x |
| **Backend** | Django REST Framework | 4.1.7 |
| **Database** | MongoDB | 6.0+ |
| **Development Environment** | GitHub Codespaces | Latest |
| **AI Assistant** | GitHub Copilot Agent Mode | Latest |

### 📋 Prerequisites

- GitHub account with Copilot access
- Basic understanding of Python and JavaScript
- Git fundamentals
- (Optional) Familiarity with Django and React

### 🚀 Getting Started

#### 1. Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/sabatinosaccomandi/skills-build-applications-w-copilot-agent-mode.git
cd skills-build-applications-w-copilot-agent-mode

# Or use GitHub Codespaces (Recommended)
# Click the "Code" button → "Codespaces" → "Create codespace on main"
```

#### 2. Backend Setup

```bash
# Create project structure
mkdir -p octofit-tracker/backend
mkdir -p octofit-tracker/frontend

# Create Python virtual environment
python3 -m venv octofit-tracker/backend/venv

# Activate virtual environment
source octofit-tracker/backend/venv/bin/activate  # Linux/Mac
# or
octofit-tracker\backend\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r octofit-tracker/backend/requirements.txt

# Start MongoDB (if not already running)
ps aux | grep mongod

# Run Django migrations
cd octofit-tracker/backend
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start Django development server
python manage.py runserver 0.0.0.0:8000
```

#### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd octofit-tracker/frontend

# Install dependencies
npm install

# Start React development server
npm start
```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

### 📁 Project Structure

```
octofit-tracker/
├── backend/
│   ├── venv/                    # Python virtual environment
│   ├── octofit_tracker/         # Django project
│   │   ├── settings.py          # Django settings
│   │   ├── urls.py              # URL routing
│   │   ├── models.py            # Database models
│   │   ├── serializers.py       # DRF serializers
│   │   ├── views.py             # API views
│   │   └── ...
│   └── requirements.txt         # Python dependencies
│
└── frontend/
    ├── public/                  # Static files
    ├── src/
    │   ├── components/          # React components
    │   ├── pages/               # Page components
    │   ├── services/            # API services
    │   ├── App.js               # Main app component
    │   └── index.js             # Entry point
    ├── package.json             # Node dependencies
    └── ...
```

### 🤖 Using GitHub Copilot Agent Mode

This project is designed to be built with GitHub Copilot Agent Mode. Here's how to use it effectively:

1. **Open Copilot Chat**: Click the Copilot icon in VS Code
2. **Select "Agent" mode**: From the dropdown menu
3. **Use structured prompts**: Reference the `.github/prompts/` directory for examples
4. **Follow instructions**: Custom instructions in `.github/instructions/` guide Copilot's responses
5. **Iterate and refine**: Agent mode can self-correct and improve based on feedback

Example prompts:
```
Let's create the User model with authentication and profile fields
```
```
Build a React component for the activity logging form
```
```
Create API endpoints for team management with CRUD operations
```

### 📖 Learning Path

This repository includes a structured learning path:

1. **Step 1**: [Preparing](/.github/steps/1-preparing.md) - Introduction to GitHub Copilot Agent Mode
2. **Step 2**: [Application Initial Setup](/.github/steps/2-application-initial-setup.md) - Project structure and dependencies
3. **Step 3**: [Django Project Setup](/.github/steps/3-django-project-setup.md) - Backend configuration
4. **Step 4**: [Django REST Framework](/.github/steps/4-setup-django-rest-framework.md) - API development
5. **Step 5**: [React Frontend](/.github/steps/5-setup-frontend-react-framework.md) - UI development
6. **Step 6**: [Copilot on GitHub](/.github/steps/6-copilot-on-github.md) - Advanced features

### 🧪 Testing

```bash
# Backend tests
cd octofit-tracker/backend
python manage.py test

# Frontend tests
cd octofit-tracker/frontend
npm test
```

### 📚 Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Using Agent Mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
- [Prompt Engineering Guide](https://docs.github.com/en/copilot/concepts/prompt-engineering)
- [Django Documentation](https://docs.djangoproject.com/)
- [React Documentation](https://react.dev/)

### 🤝 Contributing

This is an educational project. Feel free to:
- Fork the repository
- Create feature branches
- Submit pull requests
- Report issues
- Share improvements

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 👥 Acknowledgments

- Created as part of GitHub Skills learning path
- Inspired by real educational needs at Mergington High School
- Built with GitHub Copilot Agent Mode

---

## Italiano

### 📚 Panoramica

**OctoFit Tracker** è un'applicazione completa per il monitoraggio del fitness progettata per scopi educativi, specificamente per la Mergington High School. Questo progetto dimostra come costruire applicazioni web moderne utilizzando GitHub Copilot Agent Mode, combinando assistenza AI all'avanguardia con pratiche di sviluppo consolidate.

Questo repository funge sia da esercizio di apprendimento che da esempio di applicazione reale, mostrando agli sviluppatori come sfruttare le capacità autonome di GitHub Copilot per accelerare lo sviluppo su più tecnologie.

### 🎯 Scopo del Progetto

Questo progetto è stato creato per aiutare studenti e sviluppatori a:
- Imparare a costruire applicazioni web full-stack con assistenza AI
- Padroneggiare GitHub Copilot Agent Mode per lo sviluppo autonomo
- Comprendere lo stack di sviluppo web moderno (React + Django + MongoDB)
- Praticare prompt engineering e programmazione assistita da AI
- Costruire applicazioni reali che risolvono problemi concreti

### ✨ Funzionalità

- **Autenticazione e Profili Utente**: Registrazione e gestione utenti sicura
- **Registrazione e Tracciamento Attività**: Traccia varie attività fitness (corsa, camminata, allenamento forza)
- **Gestione Team**: Crea e gestisci team di fitness
- **Classifica Competitiva**: Competizione fitness gamificata con punti e classifiche
- **Suggerimenti Allenamento Personalizzati**: Raccomandazioni basate su AI in base all'attività dell'utente
- **Sistema Achievement**: Badge e traguardi per mantenere l'engagement
- **Dashboard Progressi**: Rappresentazione visuale dei progressi fitness nel tempo

### 🛠️ Stack Tecnologico

| Componente | Tecnologia | Versione |
|-----------|-----------|---------|
| **Frontend** | React.js | 18.x |
| **Backend** | Django REST Framework | 4.1.7 |
| **Database** | MongoDB | 6.0+ |
| **Ambiente di Sviluppo** | GitHub Codespaces | Latest |
| **Assistente AI** | GitHub Copilot Agent Mode | Latest |

### 📋 Prerequisiti

- Account GitHub con accesso a Copilot
- Comprensione base di Python e JavaScript
- Fondamenti di Git
- (Opzionale) Familiarità con Django e React

### 🚀 Iniziare

#### 1. Configurazione Ambiente di Sviluppo

```bash
# Clona il repository
git clone https://github.com/sabatinosaccomandi/skills-build-applications-w-copilot-agent-mode.git
cd skills-build-applications-w-copilot-agent-mode

# Oppure usa GitHub Codespaces (Raccomandato)
# Clicca il pulsante "Code" → "Codespaces" → "Create codespace on main"
```

#### 2. Configurazione Backend

```bash
# Crea struttura progetto
mkdir -p octofit-tracker/backend
mkdir -p octofit-tracker/frontend

# Crea ambiente virtuale Python
python3 -m venv octofit-tracker/backend/venv

# Attiva ambiente virtuale
source octofit-tracker/backend/venv/bin/activate  # Linux/Mac

# Installa dipendenze
pip install -r octofit-tracker/backend/requirements.txt

# Avvia server Django
python manage.py runserver 0.0.0.0:8000
```

#### 3. Configurazione Frontend

```bash
# Vai alla directory frontend
cd octofit-tracker/frontend

# Installa dipendenze
npm install

# Avvia server React
npm start
```

### 🤖 Utilizzo di GitHub Copilot Agent Mode

Questo progetto è progettato per essere costruito con GitHub Copilot Agent Mode. Ecco come usarlo efficacemente:

1. **Apri Copilot Chat**: Clicca l'icona Copilot in VS Code
2. **Seleziona modalità "Agent"**: Dal menu a discesa
3. **Usa prompt strutturati**: Fai riferimento alla directory `.github/prompts/` per esempi
4. **Segui le istruzioni**: Le istruzioni personalizzate in `.github/instructions/` guidano le risposte di Copilot
5. **Itera e perfeziona**: Agent mode può auto-correggersi e migliorare in base ai feedback

### 📄 Licenza

Questo progetto è concesso in licenza sotto la Licenza MIT - vedi il file [LICENSE](LICENSE) per i dettagli.

---

## Français

### 📚 Aperçu

**OctoFit Tracker** est une application complète de suivi de fitness conçue à des fins éducatives, spécifiquement pour le Mergington High School. Ce projet démontre comment construire des applications web modernes en utilisant GitHub Copilot Agent Mode, combinant l'assistance IA de pointe avec des pratiques de développement éprouvées.

Ce référentiel sert à la fois d'exercice d'apprentissage et d'exemple d'application réelle, montrant aux développeurs comment tirer parti des capacités autonomes de GitHub Copilot pour accélérer le développement à travers plusieurs technologies.

### 🎯 Objectif du Projet

Ce projet a été créé pour aider les étudiants et les développeurs à:
- Apprendre à construire des applications web full-stack avec assistance IA
- Maîtriser GitHub Copilot Agent Mode pour le développement autonome
- Comprendre la pile de développement web moderne (React + Django + MongoDB)
- Pratiquer l'ingénierie des prompts et le codage assisté par IA
- Construire des applications réelles qui résolvent des problèmes concrets

### ✨ Fonctionnalités

- **Authentification et Profils Utilisateur**: Inscription et gestion sécurisées des utilisateurs
- **Enregistrement et Suivi des Activités**: Suivez diverses activités de fitness (course, marche, musculation)
- **Gestion d'Équipe**: Créez et gérez des équipes de fitness
- **Classement Compétitif**: Compétition de fitness gamifiée avec points et classements
- **Suggestions d'Entraînement Personnalisées**: Recommandations basées sur l'IA selon l'activité de l'utilisateur
- **Système de Réalisations**: Badges et jalons pour maintenir l'engagement
- **Tableau de Bord des Progrès**: Représentation visuelle des progrès de fitness au fil du temps

### 🛠️ Pile Technologique

| Composant | Technologie | Version |
|-----------|-----------|---------|
| **Frontend** | React.js | 18.x |
| **Backend** | Django REST Framework | 4.1.7 |
| **Base de données** | MongoDB | 6.0+ |
| **Environnement de Développement** | GitHub Codespaces | Latest |
| **Assistant IA** | GitHub Copilot Agent Mode | Latest |

### 📋 Prérequis

- Compte GitHub avec accès à Copilot
- Compréhension de base de Python et JavaScript
- Fondamentaux de Git
- (Optionnel) Familiarité avec Django et React

### 🚀 Démarrage

#### 1. Configuration de l'Environnement de Développement

```bash
# Cloner le référentiel
git clone https://github.com/sabatinosaccomandi/skills-build-applications-w-copilot-agent-mode.git
cd skills-build-applications-w-copilot-agent-mode

# Ou utilisez GitHub Codespaces (Recommandé)
# Cliquez sur le bouton "Code" → "Codespaces" → "Create codespace on main"
```

#### 2. Configuration du Backend

```bash
# Créer la structure du projet
mkdir -p octofit-tracker/backend
mkdir -p octofit-tracker/frontend

# Créer l'environnement virtuel Python
python3 -m venv octofit-tracker/backend/venv

# Activer l'environnement virtuel
source octofit-tracker/backend/venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install -r octofit-tracker/backend/requirements.txt

# Démarrer le serveur Django
python manage.py runserver 0.0.0.0:8000
```

#### 3. Configuration du Frontend

```bash
# Naviguer vers le répertoire frontend
cd octofit-tracker/frontend

# Installer les dépendances
npm install

# Démarrer le serveur React
npm start
```

### 🤖 Utilisation de GitHub Copilot Agent Mode

Ce projet est conçu pour être construit avec GitHub Copilot Agent Mode. Voici comment l'utiliser efficacement:

1. **Ouvrir Copilot Chat**: Cliquez sur l'icône Copilot dans VS Code
2. **Sélectionner le mode "Agent"**: Dans le menu déroulant
3. **Utiliser des prompts structurés**: Référez-vous au répertoire `.github/prompts/` pour des exemples
4. **Suivre les instructions**: Les instructions personnalisées dans `.github/instructions/` guident les réponses de Copilot
5. **Itérer et affiner**: Le mode Agent peut s'auto-corriger et s'améliorer en fonction des retours

### 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Српски (Serbian)

### 📚 Преглед

**OctoFit Tracker** је свеобухватна апликација за праћење фитнеса дизајнирана у образовне сврхе, специфично за Mergington High School. Овај пројекат демонстрира како градити модерне веб апликације користећи GitHub Copilot Agent Mode, комбинујући најсавременију AI асистенцију са проверним развојним праксама.

Овај репозиторијум служи и као вежба за учење и као пример реалне апликације, показујући програмерима како да искористе аутономне способности GitHub Copilot-а да убрзају развој кроз више технологија.

### 🎯 Сврха Пројекта

Овај пројекат је креиран да помогне студентима и програмерима да:
- Науче да граде full-stack веб апликације уз AI асистенцију
- Овладају GitHub Copilot Agent Mode за аутономни развој
- Разумеју модерни веб развојни стек (React + Django + MongoDB)
- Вежбају prompt engineering и програмирање уз помоћ AI
- Граде реалне апликације које решавају стварне проблеме

### ✨ Могућности

- **Аутентификација и Кориснички Профили**: Сигурна регистрација и управљање корисницима
- **Бележење и Праћење Активности**: Прати различите фитнес активности (трчање, ходање, тренинг снаге)
- **Управљање Тимом**: Креирај и управљај фитнес тимовима
- **Конкурентна Табела**: Gamified фитнес такмичење са поенима и рангирањима
- **Персонализовани Предлози Вежби**: Препоруке засноване на AI према активности корисника
- **Систем Достигнућа**: Значке и прекретнице за одржавање ангажовања
- **Контролна Табла Напретка**: Визуелни приказ фитнес напретка током времена

### 🛠️ Технолошки Стек

| Компонента | Технологија | Верзија |
|-----------|-----------|---------|
| **Frontend** | React.js | 18.x |
| **Backend** | Django REST Framework | 4.1.7 |
| **База података** | MongoDB | 6.0+ |
| **Развојно Окружење** | GitHub Codespaces | Latest |
| **AI Асистент** | GitHub Copilot Agent Mode | Latest |

### 📋 Предуслови

- GitHub налог са приступом Copilot-у
- Основно разумевање Python-а и JavaScript-а
- Основе Git-а
- (Опционално) Познавање Django и React

### 🚀 Почетак

```bash
# Клонирај репозиторијум
git clone https://github.com/sabatinosaccomandi/skills-build-applications-w-copilot-agent-mode.git
cd skills-build-applications-w-copilot-agent-mode

# Или користи GitHub Codespaces (Препоручено)
```

### 📄 Лиценца

Овај пројекат је лиценциран под MIT лиценцом - погледајте [LICENSE](LICENSE) фајл за детаље.

---

## Shqip (Albanian)

### 📚 Përmbledhje

**OctoFit Tracker** është një aplikacion gjithëpërfshirës për ndjekjen e fitness-it i dizajnuar për qëllime edukative, specifikisht për Mergington High School. Ky projekt demonstron se si të ndërtoni aplikacione web moderne duke përdorur GitHub Copilot Agent Mode, duke kombinuar ndihmën më të avancuar AI me praktikat e provuara të zhvillimit.

Ky repository shërben si një ushtrim mësimi dhe një shembull aplikacioni real, duke u treguar zhvilluesve se si të shfrytëzojnë aftësitë autonome të GitHub Copilot për të përshpejtuar zhvillimin nëpër teknologji të shumta.

### 🎯 Qëllimi i Projektit

Ky projekt u krijua për të ndihmuar studentët dhe zhvilluesit të:
- Mësojnë të ndërtojnë aplikacione web full-stack me ndihmë AI
- Zotërojnë GitHub Copilot Agent Mode për zhvillim autonom
- Kuptojnë stack-un modern të zhvillimit web (React + Django + MongoDB)
- Praktikojnë prompt engineering dhe kodim të ndihmuar nga AI
- Ndërtojnë aplikacione reale që zgjidhin probleme konkrete

### ✨ Veçoritë

- **Autentifikimi dhe Profilet e Përdoruesit**: Regjistrimi dhe menaxhimi i sigurt i përdoruesve
- **Regjistrimi dhe Ndjekja e Aktiviteteve**: Ndjek aktivitete të ndryshme fitness (vrapim, ecje, stërvitje force)
- **Menaxhimi i Ekipit**: Krijo dhe menaxho ekipe fitness
- **Tabela e Renditjes Konkurruese**: Garë fitness e gamifikuar me pikë dhe renditje
- **Sugjerime të Personalizuara për Stërvitje**: Rekomandime të bazuara në AI sipas aktivitetit të përdoruesit
- **Sistemi i Arritjeve**: Shenja dhe objektiva për të mbajtur angazhimin
- **Paneli i Përparimit**: Prezantim vizual i përparimit të fitness-it me kalimin e kohës

### 🛠️ Stack Teknologjik

| Komponenti | Teknologjia | Versioni |
|-----------|-----------|---------|
| **Frontend** | React.js | 18.x |
| **Backend** | Django REST Framework | 4.1.7 |
| **Baza e të dhënave** | MongoDB | 6.0+ |
| **Mjedisi i Zhvillimit** | GitHub Codespaces | Latest |
| **Asistenti AI** | GitHub Copilot Agent Mode | Latest |

### 📋 Parakushtet

- Llogari GitHub me akses në Copilot
- Kuptim bazë i Python dhe JavaScript
- Bazat e Git
- (Opsionale) Njohuri me Django dhe React

### 🚀 Fillimi

```bash
# Klono repository-n
git clone https://github.com/sabatinosaccomandi/skills-build-applications-w-copilot-agent-mode.git
cd skills-build-applications-w-copilot-agent-mode

# Ose përdor GitHub Codespaces (E Rekomanduar)
```

### 📄 Licenca

Ky projekt është i licencuar nën Licencën MIT - shihni skedarin [LICENSE](LICENSE) për detaje.

---

## हिन्दी (Hindi)

### 📚 अवलोकन

**OctoFit Tracker** एक व्यापक फिटनेस ट्रैकिंग एप्लिकेशन है जो शैक्षिक उद्देश्यों के लिए डिज़ाइन किया गया है, विशेष रूप से Mergington High School के लिए। यह परियोजना दर्शाती है कि GitHub Copilot Agent Mode का उपयोग करके आधुनिक वेब एप्लिकेशन कैसे बनाए जाएं, अत्याधुनिक AI सहायता को सिद्ध विकास प्रथाओं के साथ जोड़ते हुए।

यह रिपॉजिटरी एक सीखने के अभ्यास और वास्तविक एप्लिकेशन उदाहरण दोनों के रूप में कार्य करती है, डेवलपर्स को दिखाती है कि कैसे GitHub Copilot की स्वायत्त क्षमताओं का लाभ उठाकर कई तकनीकों में विकास को तेज किया जाए।

### 🎯 परियोजना का उद्देश्य

यह परियोजना छात्रों और डेवलपर्स की मदद के लिए बनाई गई थी:
- AI सहायता के साथ full-stack वेब एप्लिकेशन बनाना सीखें
- स्वायत्त विकास के लिए GitHub Copilot Agent Mode में महारत हासिल करें
- आधुनिक वेब डेवलपमेंट स्टैक (React + Django + MongoDB) को समझें
- प्रॉम्प्ट इंजीनियरिंग और AI-सहायता प्राप्त कोडिंग का अभ्यास करें
- वास्तविक समस्याओं को हल करने वाले वास्तविक एप्लिकेशन बनाएं

### ✨ विशेषताएं

- **उपयोगकर्ता प्रमाणीकरण और प्रोफाइल**: सुरक्षित उपयोगकर्ता पंजीकरण और प्रबंधन
- **गतिविधि लॉगिंग और ट्रैकिंग**: विभिन्न फिटनेस गतिविधियों को ट्रैक करें (दौड़ना, चलना, शक्ति प्रशिक्षण)
- **टीम प्रबंधन**: फिटनेस टीमें बनाएं और प्रबंधित करें
- **प्रतिस्पर्धी लीडरबोर्ड**: अंकों और रैंकिंग के साथ गेमिफाइड फिटनेस प्रतियोगिता
- **व्यक्तिगत कसरत सुझाव**: उपयोगकर्ता गतिविधि के आधार पर AI-संचालित अनुशंसाएं
- **उपलब्धि प्रणाली**: जुड़ाव बनाए रखने के लिए बैज और मील के पत्थर
- **प्रगति डैशबोर्ड**: समय के साथ फिटनेस प्रगति का दृश्य प्रतिनिधित्व

### 🛠️ प्रौद्योगिकी स्टैक

| घटक | प्रौद्योगिकी | संस्करण |
|-----------|-----------|---------|
| **Frontend** | React.js | 18.x |
| **Backend** | Django REST Framework | 4.1.7 |
| **डेटाबेस** | MongoDB | 6.0+ |
| **विकास वातावरण** | GitHub Codespaces | Latest |
| **AI सहायक** | GitHub Copilot Agent Mode | Latest |

### 📋 पूर्वापेक्षाएँ

- Copilot एक्सेस के साथ GitHub खाता
- Python और JavaScript की बुनियादी समझ
- Git की मूल बातें
- (वैकल्पिक) Django और React से परिचित

### 🚀 शुरुआत करना

```bash
# रिपॉजिटरी क्लोन करें
git clone https://github.com/sabatinosaccomandi/skills-build-applications-w-copilot-agent-mode.git
cd skills-build-applications-w-copilot-agent-mode

# या GitHub Codespaces का उपयोग करें (अनुशंसित)
```

### 📄 लाइसेंस

यह परियोजना MIT लाइसेंस के तहत लाइसेंस प्राप्त है - विवरण के लिए [LICENSE](LICENSE) फ़ाइल देखें।

---

## 🔗 Quick Links

- **Start Exercise**: [Go to Issue #1](https://github.com/sabatinosaccomandi/skills-build-applications-w-copilot-agent-mode/issues/1)
- **GitHub Copilot**: [Learn More](https://github.com/features/copilot)
- **Documentation**: [Agent Mode Guide](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

