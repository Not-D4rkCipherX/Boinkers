const axios = require("axios");
const { log } = require("./utils"); // Adjust the path as necessary
const settings = require("./config/config");

const urlChecking = "https://raw.githubusercontent.com/D4rkCipherX/APIs-checking/refs/heads/main/endpoints.json";

async function checkBaseUrl() {
  console.log("Checking api...".blue);
  if (settings.ADVANCED_ANTI_DETECTION) {
    const result = await getBaseApi(urlChecking);
    if (result.endpoint) {
      log("No change in api!", "success");
      return result;
    }
  } else {
    return {
      endpoint: settings.BASE_URL,
      message:
        "Telegram Channel : (https://t.me/D4rkCipherX)",
    };
  }
}

async function getBaseApi(url) {
  try {
    const response = await axios.get(url);
    const content = response.data;
    if (content?.magic) {
      return { endpoint: content.magic, message: content.copyright };
    } else {
      return {
        endpoint: null,
        message:
          "Telegram Channel : (https://t.me/D4rkCipherX)",
      };
    }
  } catch (e) {
    return {
      endpoint: null,
      message:
      "Telegram Channel : (https://t.me/D4rkCipherX)",
    };
  }
}

module.exports = { checkBaseUrl };
