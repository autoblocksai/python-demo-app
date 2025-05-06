<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.autoblocks.ai/images/logos/dark.png">
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.autoblocks.ai/images/logos/light.png">
    <img alt="Autoblocks Logo" width="300px" src="https://cdn.autoblocks.ai/images/logos/light.png">
  </picture>
</p>
<p align="center">
  📚
  <a href="https://docs.autoblocks.ai/">Documentation</a>
  &nbsp;
  •
  &nbsp;
  🖥️
  <a href="https://app-v2.autoblocks.ai/">Application</a>
  &nbsp;
  •
  &nbsp;
  🏠
  <a href="https://www.autoblocks.ai/">Home</a>
</p>

# Development Setup

* Install [`pyenv`](https://github.com/pyenv/pyenv)
  * Install python 3.12: `pyenv install 3.12`
* Install [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv)
* Install [`poetry`](https://python-poetry.org/docs/#installation)
* Create a virtualenv: `pyenv virtualenv 3.12 python-demo-app`
  * Activate the virtualenv: `pyenv activate python-demo-app`
* Install dependencies: `poetry install`
* Install pre-commit: `poetry run pre-commit install`

# Running the app

## Create app in Autoblocks

Create a new app of type Prompt named "Doctor GPT" in the Autoblocks platform.

Next you will need to create the following prompts and deploy them:

### clinical_answerer

**Model Parameters:**

- Model: `gpt-4o`

**Templates:**

`system`
```
You are an expert medical assistant. Answer the doctor's question clearly and concisely using up-to-date general medical knowledge.
If you are not confident, say: "I'm not sure. Please refer to clinical guidelines."
```

`user`
```
Doctor's Question:
{{ doctor_message }}
```

### doctor_intent_classifier

**Model Parameters:**

- Model: `gpt-4o`
- Temperature: `0`

**Templates:**

`system`
```
You are an AI assistant helping a doctor. Classify the doctor's question or request into one of the following types:

- Generate SOAP Note
- Suggest Follow-Up Questions
- Summarize Patient History
- Answer Clinical Question
- Summarize Visit
- Other

Respond only with the category.
```

`user`
```
Doctor Input:
{{ doctor_message }}
```

### patient_history_summarizer

**Model Parameters:**

- Model: `gpt-4o`

**Templates:**

`system`
```
You are helping a doctor quickly review a patient's history based on notes and transcripts.
Focus on major illnesses, surgeries, medications, allergies, and family history.
```

`user`
```
Summarize the patient's medical history from this text:
{{ transcript_or_notes }}
```

### soap_generator

**Model Parameters:**

- Model: `gpt-4o`

**Templates:**

`system`
```
You are a medical assistant. Based on the following transcript between a doctor and patient, create a SOAP note.
Respond only with the SOAP note, clearly labeled:
Subjective:
Objective:
Assessment:
Plan:
```

`user`
```
Transcript:
{{ transcript }}
```

### visit_summary_writer

**Model Parameters:**

- Model: `gpt-4o`

**Templates:**

`system`
```
You are preparing a quick summary of a doctor's visit to help update medical records.
Focus on major complaints, findings, and follow-up plans.
```

`user`
```
Write a short, clear visit summary based on this text:
{{ transcript_or_notes }}
```

## Set environment variables

You can either create a `.env` file (copy from `.env.example`) in the root of the project or set the following environment variables:

```bash
export AUTOBLOCKS_TEST_RUN_MESSAGE="Made prompt more concise"
```

```bash
export AUTOBLOCKS_V2_API_KEY=<your-api-key>
```

**Note:** You can get your Autoblocks API key from the [Autoblocks settings page](https://app-v2.autoblocks.ai/settings/api-keys).

```bash
export OPENAI_API_KEY=<your-api-key>
```

**Note:** You can get your OpenAI API key from the [OpenAI dashboard](https://platform.openai.com/api-keys).

## Run the tests

```bash
poetry run run_tests
```

## Running in CI

First, fork the repository to your own GitHub account.

Then, set the following repository secrets:

1. `AUTOBLOCKS_V2_API_KEY`
2. `OPENAI_API_KEY`

**Note:** You can view how these are used in the [`.github/workflows/autoblocks_tests.yml`](.github/workflows/autoblocks_tests.yml) file.

Now you can run the workflow in the Actions tab on the GitHub UI.

## View results

Go to your application at [app-v2.autoblocks.ai](https://app-v2.autoblocks.ai) and view the results.
