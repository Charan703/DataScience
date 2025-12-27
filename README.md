# 🍷 Wine Quality Prediction - End to End ML Project

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="ML">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</div>

## 📊 Project Overview

This project implements a complete **Machine Learning pipeline** for predicting wine quality using various physicochemical properties. The system follows MLOps best practices with modular architecture and automated workflows.

## 🎯 Features

- 🔄 **Automated ML Pipeline** - End-to-end workflow from data ingestion to model deployment 
- 📈 **Data Validation** - Comprehensive data quality checks and schema validation
- 🔧 **Feature Engineering** - Advanced data transformation and preprocessing
- 🤖 **Model Training** - ElasticNet regression with hyperparameter tuning
- 📊 **Model Evaluation** - Performance metrics with MLflow experiment tracking
- 📈 **MLflow Integration** - Model versioning and experiment management with DagsHub
- 🚀 **Web Interface** - Flask-based prediction API
- 🐳 **Containerized** - Docker support for easy deployment

## 🏗️ ML Pipeline Architecture

```mermaid
graph LR
    A[📥 Data Ingestion] --> B[✅ Data Validation]
    B --> C[🔄 Data Transformation]
    C --> D[🎯 Model Training]
    D --> E[📊 Model Evaluation]
    E --> F[🚀 Deployment]
```

## 📋 File Flow Architecture

```mermaid
graph TD
    A[config.yaml] --> B[ConfigurationManager]
    C[params.yaml] --> B
    D[schema.yaml] --> B
    
    B --> E[DataIngestionConfig]
    B --> F[DataValidationConfig]
    B --> G[DataTransformationConfig]
    
    E --> H[DataIngestion Component]
    F --> I[DataValidation Component]
    G --> J[DataTransformation Component]
    
    H --> K[DataIngestionTrainingPipeline]
    I --> L[DataValidationTrainingPipeline]
    J --> M[DataTransformationTrainingPipeline]
    
    K --> N[main.py]
    L --> N
    M --> N
    
    N --> O[artifacts/]
    O --> P[data_ingestion/]
    O --> Q[data_validation/]
    O --> R[data_transformation/]
    
    S[app.py] --> T[Flask Web Interface]
    O --> T
```

## 🔄 Component Interaction Flow

```mermaid
sequenceDiagram
    participant M as main.py
    participant DI as DataIngestionPipeline
    participant DV as DataValidationPipeline
    participant DT as DataTransformationPipeline
    participant MT as ModelTrainerPipeline
    participant ME as ModelEvaluationPipeline
    participant C as Components
    participant A as Artifacts
    participant ML as MLflow
    
    M->>DI: 1. Start Data Ingestion
    DI->>C: Load DataIngestion Component
    C->>A: Download & Extract Data
    DI-->>M: Complete
    
    M->>DV: 2. Start Data Validation
    DV->>C: Load DataValidation Component
    C->>A: Validate Schema & Quality
    DV-->>M: Complete
    
    M->>DT: 3. Start Data Transformation
    DT->>C: Load DataTransformation Component
    C->>A: Transform & Preprocess
    DT-->>M: Complete
    
    M->>MT: 4. Start Model Training
    MT->>C: Load ModelTrainer Component
    C->>A: Train ElasticNet Model
    MT-->>M: Complete
    
    M->>ME: 5. Start Model Evaluation
    ME->>C: Load ModelEvaluation Component
    C->>ML: Log Metrics & Model
    C->>A: Save Evaluation Results
    ME-->>M: Complete
```

### 🔄 Workflow Steps

| Step | Description | Status |
|------|-------------|--------|
| 1️⃣ | **Data Ingestion** - Download and extract wine quality dataset | ✅ |
| 2️⃣ | **Data Validation** - Validate schema and data quality | ✅ |
| 3️⃣ | **Data Transformation** - Feature engineering and preprocessing | ✅ |
| 4️⃣ | **Model Training** - Train ML models with cross-validation | ✅ |
| 5️⃣ | **Model Evaluation** - Performance metrics and MLflow tracking | ✅ |

## 🛠️ Development Workflow

### 📋 Step-by-Step Implementation Guide

1. 📝 **Update config.yaml** - Configure paths and parameters
2. 📋 **Update schema.yaml** - Define data schema and validation rules
3. ⚙️ **Update params.yaml** - Set model hyperparameters
4. 🏗️ **Update the entity** - Define data classes and configurations
5. 🔧 **Update configuration manager** - Handle config loading in src/config
6. 🧩 **Update components** - Implement core ML components
7. 🔄 **Update pipeline** - Create training and prediction pipelines
8. 🚀 **Update main.py** - Orchestrate the entire workflow

## 📁 Project Structure

```
📦 DataScience/
├── 📂 artifacts/           # Generated outputs and models
├── 📂 config/             # Configuration files
│   ├── config.yaml        # Main configuration
│   ├── params.yaml        # Model parameters
│   └── schema.yaml        # Data schema
├── 📂 research/           # Jupyter notebooks for experimentation
├── 📂 src/Data_Science/   # Source code
│   ├── 📂 components/     # ML pipeline components
│   ├── 📂 config/         # Configuration management
│   ├── 📂 entity/         # Data classes and entities
│   ├── 📂 pipeline/       # Training and prediction pipelines
│   └── 📂 utils/          # Utility functions
├── 📂 templates/          # HTML templates for web interface
├── 📄 app.py             # Flask web application
├── 📄 main.py            # Main training script
└── 📄 requirements.txt   # Python dependencies
```

## 🚀 Quick Start

### 1️⃣ Clone Repository
```bash
git clone <repository-url>
cd DataScience
```

### 2️⃣ Setup Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run Training Pipeline
```bash
python main.py
```

### 4️⃣ Start Web Application
```bash
python app.py
```

## 🐳 Docker Deployment

```bash
# Build Docker image
docker build -t wine-quality-predictor .

# Run container
docker run -p 8080:8080 wine-quality-predictor
```

## 📊 Dataset Information

🍷 **Wine Quality Dataset**
- **Source**: UCI Machine Learning Repository
- **Features**: 11 physicochemical properties
- **Target**: Wine quality score (0-10)
- **Samples**: ~4,900 wine samples

### 🔍 Key Features:
- Fixed acidity
- Volatile acidity  
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to branch (`git push origin feature/amazing-feature`)
5. 🔄 Open Pull Request

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🎓 Dataset provided by UCI Machine Learning Repository
- 🛠️ Built with Python, Flask, and Scikit-learn
- 🐳 Containerized with Docker for easy deployment

---

<div align="center">
  <p>Made with ❤️ for Machine Learning enthusiasts</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>
