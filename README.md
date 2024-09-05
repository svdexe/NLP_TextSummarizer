# End-to-end Text Summarization Development to Deployment

## 🌟 Introduction

In our information-rich world, the ability to quickly distill key points from lengthy texts is invaluable. Text summarization, a cutting-edge application of Natural Language Processing (NLP), addresses this need by condensing vast amounts of information into concise, meaningful summaries. This project showcases the development and deployment of a state-of-the-art text summarization model, bridging the gap between advanced NLP techniques and practical, real-world applications.

## 🔍 Project Overview

This repository offers a comprehensive, end-to-end journey through the creation of a powerful text summarization tool. We delve into the intricate process of fine-tuning a HuggingFace Transformer model on custom data, optimizing it for superior performance in summarization tasks. The project doesn't stop at model development; it extends to deployment on Amazon Web Services (AWS), demonstrating how to bring a machine learning model from concept to production.

Key aspects covered in this project include:

- In-depth exploration of Large Language Model (LLM) fine-tuning techniques
- Detailed description of the dataset used for training
- Step-by-step project timeline and setup instructions
- Comprehensive breakdown of development phases
- Insights into AWS deployment strategies

Moreover, this project serves as a practical guide to implementing industry-standard practices in software development and MLOps, including modular coding, containerization with Docker, and setting up robust CI/CD pipelines.

## 🚀 Features

Our text summarization project boasts a range of features designed to showcase both the power of NLP and best practices in software development:

1. **Advanced Model Fine-tuning**: 
   - Leverage the HuggingFace Transformer architecture for state-of-the-art summarization capabilities
   - Custom data integration for domain-specific summarization tasks

2. **Cloud-based Deployment**:
   - Harness the power of AWS services including EC2 and ECR for scalable, reliable deployment
   - Implement GitHub Actions for streamlined cloud integration

3. **Modular and Maintainable Code Structure**:
   - Employ best practices in software engineering for clean, organized code
   - Enhance long-term maintainability and ease of future improvements

4. **Interactive User Interface**:
   - Seamless integration with FastAPI to create an intuitive, responsive frontend
   - Real-time summarization capabilities accessible through a user-friendly web interface

5. **Robust CI/CD Pipeline**:
   - Utilize GitHub Actions for automated testing, building, and deployment
   - Ensure consistent code quality and streamline the development-to-production workflow

6. **Containerized Application**:
   - Dockerized deployment for consistency across different environments
   - Simplified scaling and management of application dependencies
  
7. **Cloud-based Model Training**:
   - Train the model directly through the API after deployment
   - Leverage powerful AWS servers for improved training performance
   - Enables continuous model improvement without redeployment
  
   

This project not only delivers a powerful text summarization tool but also serves as a comprehensive template for developing and deploying sophisticated NLP applications in a production environment.


## 🖥️ Applications

This project includes two different applications:

1. **Default FastAPI App**: A standard implementation using FastAPI.
2. **Custom App (zapp.py)**: An enhanced version with animations and responsive CSS.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Conda (recommended for environment management)

### Installation and Usage

1. Clone the repository:
   ```
   git clone https://github.com/entbappy/End-to-end-Text-Summarization.git
   cd End-to-end-Text-Summarization
   ```

2. Create and activate a Conda environment:
   ```
   conda create -n summary python=3.8 -y
   conda activate summary
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   - For the default FastAPI app:
     ```
     python app.py
     ```
   - For the custom app with animations:
     ```
     python zapp.py
     ```

5. Open your web browser and navigate to the local host and port displayed in the console.

## Cloud-based Model Training

### After deploying the application on AWS:
1. Access the training endpoint: POST /train
2. Provide training parameters in the request body (details in API documentation)
3. Monitor training progress through the provided logs
4. Once training is complete, the API will automatically use the updated model

## 🖥️ Usage

1. Enter or paste your text in the provided textarea
2. Click "Summarize" to generate a summary
3. View the generated summary below the input area
4. (Optional) Initiate model training for improved performance

## 🔗 API Access

- **Endpoint**: `POST /predict`
- **Content-Type**: `application/json`
- **Request Body**:
  ```json
  {
  "epochs": 10,
  "batch_size": 32,
  "learning_rate": 0.001
  }
  ```

For full API documentation, visit `/docs` when the server is running.

## 📊 Model Performance

- ROUGE-1: 0.022373
- ROUGE-2: 0.0
- ROUGE-L: 0.02209
- ROUGE-Lsum: 0.02219

**Note**: Due to hardware resource constraints, this model was not fully trained to save time. Full training typically takes 12 hours or more. The current performance metrics reflect a partially trained model. You can achieve significantly better results by training the model on more powerful AWS servers after deployment.


## 🚢 AWS Deployment with GitHub Actions

### Workflow Steps

1. Update `config.yaml`
2. Update `params.yaml`
3. Update entity
4. Update the configuration manager in `src/config`
5. Update the components
6. Update the pipeline
7. Update `main.py`
8. Update `app.py`

### AWS Setup

1. Log in to AWS console
2. Create an IAM user for deployment with the following access:
   - EC2 access (virtual machine)
   - ECR (Elastic Container Registry) access
3. Create an ECR repository to store the Docker image
4. Launch an EC2 instance (Ubuntu)
5. Install Docker on the EC2 instance:
   ```
   sudo apt-get update -y
   sudo apt-get upgrade
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```
6. Configure EC2 as a self-hosted runner for GitHub Actions
7. Choose an EC2 instance type with sufficient computing power for model training (e.g., GPU-enabled instances for faster training)

### GitHub Secrets Setup

Set up the following secrets in your GitHub repository:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (e.g., us-east-1)
- `AWS_ECR_LOGIN_URI` (e.g., 566373416292.dkr.ecr.ap-south-1.amazonaws.com)
- `ECR_REPOSITORY_NAME` (e.g., simple-app)

## 🚧 Future Improvements

- [ ] Implement user accounts and history
- [ ] Add support for multiple languages
- [ ] Optimize for mobile devices
- [ ] Integrate with cloud storage services
- [ ] Complete full model training for improved performance
- [ ] Enable cloud-based model training for continuous improvement
- [ ]  Implement automated periodic training using AWS Lambda

## 👨‍💻 Contributor

- Shivam Dali is a Data Science graduate student from Adelaide University. Connect with him on [LinkedIn](https://www.linkedin.com/in/shivam-dali-86b0a1201/) and explore more projects on [GitHub](https://https://github.com/svdexe).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Krish Naik](https://github.com/krishnaik06) for the inspiring tutorial
- [FastAPI](https://fastapi.tiangolo.com/) for the efficient backend framework
- [Hugging Face](https://huggingface.co/) for the PEGASUS model


## Additional Resources
- [Medium Article](https://medium.com/@pratishsmashankar/end-to-end-text-summarization-development-to-deployment-project-review-83f9d28e40af) - Read the detailed project review on Medium.
- [GitHub Repository](https://github.com/svdexe/NLP_TextSummarizer)) - Access the code and project files.
- [LinkedIn](https://www.linkedin.com/in/shivam-dali-86b0a1201/) - Connect with me on LinkedIn.

## Tutorial Link
I followed this tutorial: [End To End NLP Project Implementation With Deployment Github Action- Text Summarization- Krish Naik](https://www.youtube.com/watch?v=p7V4Aa7qEpw&t=11054s&pp=ygUTZW5kIHRvIGVuZCAgbmxwIHN1bQ%3D%3D)





<p align="center">Made by Shivam Dali</p>
