# Training with Python for Data Engineering

## 1. Automation

- **Key findings:** Automation of the process of registering thousands of products on a platform using Python to be executed daily and on demand.

## 2. Data Analysis

- **Key findings:** Customer churn analysis through Jupyter with graphs and dashboards to identify the main causes of churn and possible improvement actions that would reduce the rate from 56% to 18%.

## 3. Artificial Intelligence

- **Key findings:** Creation of an AI capable of predicting the credit rating of a financial corporation's customers with 86% accuracy based on customer characteristics.

## 4. Creating of a Site/App

- **Key findings:** Creation of a live chat for the website and app using the Flet tool, for both frontend and backend.

## Bash Script for Libraries

Mesmo utilizando o comando `source`, o ambiente virtual ficará ativo somente dentro do script no momento em que ele estiver sendo executado. Assim que ele finalizar a execução, o terminal voltará ao normal.

Isso acontece porque:

```
Terminal
 └── script.sh (subshell)
       └── venv activated here
```

Quando o script acaba, o subshell morre.

Para que o ambiente virtual fique ativo no terminal, é preciso utilizar o seguinte comando:

```bash
chmod +x script.sh

source script.sh
```