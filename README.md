# YouTube Subscriptions Analyzer

YouTube Subscriptions Analyzer is a Python script that authenticates with the YouTube API, fetches a user's subscriptions, and visualizes the distribution of topics in a pie chart.

## Features

- Retrieves a user's YouTube subscriptions
- Aggregates topics across all subscriptions
- Visualizes the distribution of topics in a pie chart

## Requirements

- Python 3.6 or higher
- Google API credentials
- Libraries: google-auth-oauthlib, googleapiclient, matplotlib

## Setup

1. **Clone the Repository**:
   ```
   git clone https://github.com/kwisser/YoutubeSubscriptions.git
   cd youtube-subscriptions-analyzer
   ```

2. **Install Dependencies**:
   \`\`\`bash
   pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client matplotlib
   \`\`\`

3. **Set up Google API credentials**:
   - Visit the [Google Developer Console](https://console.developers.google.com/).
   - Create a project and set up the YouTube API v3 credentials.
   - Download the `client_secret.json` file and place it in the project's root directory.

## Usage

Run the script with:

\`\`\`bash
python main.py
\`\`\`

Follow the on-screen instructions to authenticate with your Google account. The script will fetch your YouTube subscriptions and generate a pie chart.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is free to use under the [MIT License](LICENSE).
