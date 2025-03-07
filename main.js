const fs = require("fs");
const path = require("path");
const axios = require("axios");
const colors = require("colors");
const readline = require("readline");
const { DateTime } = require("luxon");
const { HttpsProxyAgent } = require("https-proxy-agent");
const user_agents = require("./config/userAgents");
const settings = require("./config/config");
const { sleep, loadData, getRandomNumber, isTokenExpired, saveToken } = require("./utils");
const { Worker, isMainThread, parentPort, workerData } = require("worker_threads");
const { checkBaseUrl } = require("./checkAPI");

class Boink {
  constructor(queryId, accountIndex, proxy, baseURL, tokens) {
    this.headers = {
      Accept: "application/json, text/plain, */*",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
      "Content-Type": "application/json",
      Origin: "https://boink.boinkers.co",
      Referer: "https://boink.boinkers.co/",
      "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
      "Sec-Ch-Ua-Mobile": "?0",
      "Sec-Ch-Ua-Platform": '"Windows"',
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
      Cookie:
        "cboink.production.sid=s%3AdW4oO4-ZV4lfgCgC6CoyJV3ZwUWpvEIQ.vo6IaR00WYVlINdo7KofNspXnS5gVwQTgRgJm4BLD7w; _ga=GA1.1.316220204.1741159032; cf_clearance=L3ICbRgcqnUHg7BHJ20qyNioj1FriMsg3ca9JrQd.j8-1741159034-1.2.1.1-eRrx1yH4NekFdqFXA.6O44_5QmmZStt_yPhTcAKLnKIjB0Pg4HdnwnjKewXLoGqp_pQVdQUpZCOFwUV4Il6YvCpRdXCtlg7feso3VUiw2Xjb8OY4dTuB8WfAqoJJTqE2GGUiIK.ZMBmEtT3C8ErD3_NICzUmfrMzgl47krEzsOrsybpuabSXU.OgiuMU.12TDUfwKZr_b8hzZRXthtkGcibC1zC.OVrHyyU.x5csMwnzKNsmRhmd.YgScBmsYpo0MX_CLJUmOG8O7ucAPuYl2BScJDv48bcr6etrSqSkJhNsYa3YcakvplDS24cYkkxmEGU6A1Ji9gAsZLE93dyrBWYOUPV6IDn9TjcMs0BG6Xa8hUdSt9GSci0pswc10cMT4.oTG59zwNJHC9nLYWrjo0QNkO8dldcpmeJYmZlJPsk; _fbp=fb.1.1741159033196.450173099943643160; inpu1=1; ucc1=16; _ga_QGGLFFQ8M4=GS1.1.1741159031.1.1.1741159281.0.0.0; mp_8e903983fa8144170b628a5e084a2be3_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A195652a65c9b18-0e873eca3431bd-4c657b58-144000-195652a65c9b18%22%2C%22%24device_id%22%3A%20%22195652a65c9b18-0e873eca3431bd-4c657b58-144000-195652a65c9b18%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22__timers%22%3A%20%7B%22AppLoadingEnded%22%3A%201741159281810%7D%2C%22__alias%22%3A%20%2266e029cb499508f3cd5cc89e%22%2C%22%24user_id%22%3A%20%2266e029cb499508f3cd5cc89e%22%2C%22abClass%22%3A%20%22b%22%2C%22%24name%22%3A%20%22huyautomation2x%22%2C%22chatId%22%3A%205749675527%2C%22provider%22%3A%20%22telegram%22%2C%22currencySoft%22%3A%20993777%2C%22currencyCrypto%22%3A%202596191.7973676664%2C%22currentBoinkerId%22%3A%20%22Anubis%22%2C%22currentBoinkerLevel%22%3A%203%2C%22currentBoinkerLastUpdate%22%3A%20%222025-03-05T07%3A17%3A28.019Z%22%2C%22lastUpdateCompletedBoinkers%22%3A%20%222025-03-05T07%3A17%3A28.019Z%22%2C%22countOfCompletedBoinkers%22%3A%2010%2C%22lastLoginDate%22%3A%20%222025-03-05T07%3A17%3A28.498Z%22%2C%22registrationDate%22%3A%20%222024-09-10T11%3A13%3A15.621Z%22%2C%22daysSinceRegistration%22%3A%20175%2C%22slotMachineEnergy%22%3A%2010%2C%22slotMachineEnergyUsed%22%3A%20411%2C%22slotMachineBetsDone%22%3A%2076%2C%22slotMachineLastUpdated%22%3A%20%222024-10-18T04%3A41%3A24.915Z%22%2C%22wheelOfFortuneEnergy%22%3A%200%2C%22wheelOfFortuneLastUpdated%22%3A%20%222024-09-13T00%3A15%3A30.139Z%22%2C%22inviterId%22%3A%20%2266dfed5fcf59c389dfcaac27%22%2C%22isInvited%22%3A%20true%2C%22isWalletConnected%22%3A%20true%2C%22locale%22%3A%20%22en%22%2C%22platform%22%3A%20%22tdesktop%22%2C%22isTelegram%22%3A%20true%2C%22countOfPurchases%22%3A%200%2C%22lastPurchaseDate%22%3A%200%2C%22lastPurchaseValue%22%3A%200%2C%22maxPurchaseValue%22%3A%200%2C%22totalUSDValue%22%3A%200%7D",
    };
    this.baseURL = baseURL;
    this.queryId = queryId;
    this.accountIndex = accountIndex;
    this.proxy = proxy;
    this.proxyIP = null;
    this.session_name = null;
    this.session_user_agents = this.#load_session_data();
    this.skipTasks = settings.SKIP_TASKS;
    this.tokens = tokens;
    this.token = null;
  }
  #load_session_data() {
    try {
      const filePath = path.join(process.cwd(), "session_user_agents.json");
      const data = fs.readFileSync(filePath, "utf8");
      return JSON.parse(data);
    } catch (error) {
      if (error.code === "ENOENT") {
        return {};
      } else {
        throw error;
      }
    }
  }

  #get_random_user_agent() {
    const randomIndex = Math.floor(Math.random() * user_agents.length);
    return user_agents[randomIndex];
  }

  #get_user_agent() {
    if (this.session_user_agents[this.session_name]) {
      return this.session_user_agents[this.session_name];
    }

    this.log(`Tạo user agent...`);
    const newUserAgent = this.#get_random_user_agent();
    this.session_user_agents[this.session_name] = newUserAgent;
    this.#save_session_data(this.session_user_agents);
    return newUserAgent;
  }

  #save_session_data(session_user_agents) {
    const filePath = path.join(process.cwd(), "session_user_agents.json");
    fs.writeFileSync(filePath, JSON.stringify(session_user_agents, null, 2));
  }

  #get_platform(userAgent) {
    const platformPatterns = [
      { pattern: /iPhone/i, platform: "ios" },
      { pattern: /Android/i, platform: "android" },
      { pattern: /iPad/i, platform: "ios" },
    ];

    for (const { pattern, platform } of platformPatterns) {
      if (pattern.test(userAgent)) {
        return platform;
      }
    }

    return "Unknown";
  }

  set_headers() {
    const platform = this.#get_platform(this.#get_user_agent());
    this.headers["sec-ch-ua"] = `"Not)A;Brand";v="99", "${platform} WebView";v="127", "Chromium";v="127`;
    this.headers["sec-ch-ua-platform"] = platform;
    this.headers["User-Agent"] = this.#get_user_agent();
  }

  createUserAgent() {
    const telegramauth = this.queryId;
    const userData = JSON.parse(decodeURIComponent(telegramauth.split("user=")[1].split("&")[0]));
    this.session_name = userData.id;
    this.#get_user_agent();
  }
  loadProxies() {
    try {
      return fs.readFileSync("proxy.txt", "utf8").split("\n").filter(Boolean);
    } catch (error) {
      this.log("Could not read file proxy.txt","error");
      return [];
    }
  }

  getNextProxy() {
    return this.proxy;
  }

  async log(msg, type = "info") {
    const accountPrefix = `[Account ${this.accountIndex + 1}]`;
    let ipPrefix = "[Local IP]";
    if (settings.USE_PROXY) {
      ipPrefix = this.proxyIP ? `[${this.proxyIP}]` : "[Unknown IP]";
    }
    let logMessage = "";

    switch (type) {
      case "success":
        logMessage = `${accountPrefix}${ipPrefix} ${msg}`.green;
        break;
      case "error":
        logMessage = `${accountPrefix}${ipPrefix} ${msg}`.red;
        break;
      case "warning":
        logMessage = `${accountPrefix}${ipPrefix} ${msg}`.yellow;
        break;
      case "custom":
        logMessage = `${accountPrefix}${ipPrefix} ${msg}`.magenta;
        break;
      default:
        logMessage = `${accountPrefix}${ipPrefix} ${msg}`.blue;
    }
    console.log(logMessage);
  }
  async makeRequest(
    url,
    method,
    data = {},
    options = {
      retries: 0,
      isAuth: false,
    }
  ) {
    const { retries, isAuth } = options;

    const headers = {
      ...this.headers,
    };

    if (!isAuth) {
      headers["authorization"] = this.token;
    }

    let proxyAgent = null;
    if (settings.USE_PROXY) {
      proxyAgent = new HttpsProxyAgent(this.proxy);
    }
    let currRetries = 0,
      success = false;
    do {
      try {
        const response = await axios({
          method,
          url: `${url}${isAuth ? "" : "?p=unknown&v=2037265378"}`,
          data,
          headers,
          httpsAgent: proxyAgent,
          timeout: 30000,
        });
        success = true;
        if (response?.data?.data) return { success: true, data: response.data.data };
        return { success: true, data: response.data };
      } catch (error) {
        if (error.status < 500 && error.status >= 400 && error.status != 429) {
          // this.log(`Invalid request for ${url}, maybe have new update from server | contact: https://t.me/D4rkCipherX to get new update!`, "error");
          return { success: false, status: error.status, error: error.response.data.error || error.response.data.message || error.message };
        }
        this.log(`Request failed: ${url} | ${error.response.data ? JSON.stringify(error.response.data) : error.message} | retrying...`, "warning");
        success = false;
        await sleep(settings.DELAY_BETWEEN_REQUESTS);
        if (currRetries == retries) return { success: false, error: error.message };
      }
      currRetries++;
    } while (currRetries <= retries && !success);
  }

  async auth() {
    return this.makeRequest(
      `${this.baseURL}/public/users/loginByTelegram?tgWebAppStartParam=boink1092680235&p=tdesktop`,
      "post",
      { initDataString: this.queryId, tokenForSignUp: "" },
      { isAuth: true }
    );
  }

  async getUserData() {
    return this.makeRequest(`${this.baseURL}/api/users/me`, "get");
  }

  async getConfig() {
    return this.makeRequest(`${this.baseURL}/public/data/config`, "get");
  }

  async upgradeBoinker() {
    return this.makeRequest(`${this.baseURL}/api/boinkers/upgradeBoinker`, "post", {
      isUpgradeCurrentBoinkerToMax: true,
    });
  }

  async addShitBooster(payload) {
    return this.makeRequest(`${this.baseURL}/api/boinkers/addShitBooster`, "post", payload);
  }

  async spin(type = "spinSlotMachine", spinAmount) {
    return this.makeRequest(`${this.baseURL}/api/play/spin${type.charAt(0).toUpperCase() + type.slice(1)}/${spinAmount}`, "post", {});
  }

  async getTasks() {
    return this.makeRequest(`${this.baseURL}/api/rewardedActions/mine`, "get");
  }

  async getTasksCompleted() {
    return this.makeRequest(`${this.baseURL}/api/rewardedActions/getRewardedActionList`, "get");
  }

  async completeTask(id) {
    return this.makeRequest(`${this.baseURL}/api/rewardedActions/rewardedActionClicked/${id}`, "post", {});
  }

  async claimTask(id) {
    return this.makeRequest(`${this.baseURL}/api/rewardedActions/claimRewardedAction/${id}`, "post", {});
  }

  async clickAds(id) {
    return this.makeRequest(`${this.baseURL}/api/rewardedActions/rewardedActionClicked/${id}`, "post", {});
  }

  async watchAd(payload) {
    return this.makeRequest(`${this.baseURL}/api/rewardedActions/ad-watched`, "post", payload);
  }

  async loginByTelegram() {
    try {
      const response = await this.auth();
      if (response.success) {
        return { success: true, token: response.data.token };
      } else {
        return { success: false, status: response.status };
      }
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  async handleUpgradeBoinker() {
    try {
      // const configResult = await this.getConfig();
      const response = await this.upgradeBoinker();
      if (response.success) {
        const { newSoftCurrencyAmount, newSlotMachineEnergy, rank } = response.data;
        // if (newSoftCurrencyAmount < configResult.data?.)
        this.log(`Upgrade successful, Coin: ${newSoftCurrencyAmount} | Spin: ${newSlotMachineEnergy} | Rank: ${rank}`, "success");
return { success: true };
} else {
this.log(`Upgrade failed, insufficient balance!`, "warning");
        return { success: false };
      }
    } catch (error) {
      this.log(`Not enough coins to upgrade!`, "error");
      return { success: false, error: error.message };
    }
  }

  async claimBooster(spin) {
    const payload = spin > 30 ? { multiplier: 2, optionNumber: 3 } : { multiplier: 2, optionNumber: 1 };

    try {
      const response = await this.addShitBooster(payload);
      if (response.success) {
        const result = response.data;
        let nextBoosterTime = result.boinker?.booster?.x2?.lastTimeFreeOptionClaimed ? DateTime.fromISO(result.boinker.booster.x2.lastTimeFreeOptionClaimed) : null;
        if (nextBoosterTime) {
          nextBoosterTime = nextBoosterTime.plus({ hours: 2, minutes: 5 });
        }
        this.log(`Buy boosts successfully! Coin: ${result.userPostBooster.newCryptoCurrencyAmount || 0}`, "success");
this.log(`Rank: ${result.userPostBooster.rank}`, "info");
if (nextBoosterTime) {
this.log(`Buy next boosts on: ${nextBoosterTime.toLocaleString(DateTime.DATETIME_MED)}`, "info");
} else {
this.log(`Unable to determine next boost purchase time.`, "warning");
        }

        return { success: true, nextBoosterTime };
      } else {
        this.log(`Error when buying boosts!`, "error");
return { success: false, error: "API error" };
}
} catch (error) {
this.log(`Error when sending request to buy boosts: ${error.message}`, "error");
      return { success: false, error: error.message };
    }
  }

  async spinSlotMachine(type, spins) {
    const spinAmounts = [1000, 500, 150, 50, 25, 10, 5, 1];
    let remainingSpins = spins;
    while (remainingSpins > 0) {
      let spinAmount = spinAmounts.find((amount) => amount <= remainingSpins) || 1;
      try {
        const response = await this.spin(type, spinAmount);
        if (response.success) {
          const result = response.data;
          this.log(
            `Spin successful (${result.outcome}): Coin: ${result.newSoftCurrencyAmount.toString().white}${` | Shit: `.magenta}${result.newCryptoCurrencyAmount.toFixed(2).white}`.magenta,
"custom"
);
remainingSpins -= spinAmount;
} else {
this.log(`Error when spinning: Status code ${response.status}`, "error");
break;
}
} catch (error) {
this.log(`Error when sending spin request: ${error.message}`, "error");
        break;
      }

      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }

  async performRewardedActions() {
    try {
      const userInfoResponse = await this.getUserData();
      if (!userInfoResponse.success) {
        this.log(`Failed to get user info. Status code: ${userInfoResponse.status}`, "error");
return;
}
const userInfo = userInfoResponse.data;

this.log("Getting task list...", "info");
const response = await this.getTasks();
const responseTasks = await this.getTasksCompleted();

if (!response.success || !responseTasks.success) {
this.log(`Failed to get task list. Status code:${response.status}`, "error");
        return;
      }
      let tasksTodo = [];
      let rewardedActions = responseTasks.data;
      let tasks = Object.values(response.data);
      for (const task of tasks) {
        if (!task?.claimDateTime) {
          const isFound = rewardedActions.find((i) => i.nameId == task.nameId);
          if (isFound) {
            tasksTodo.push({ ...isFound, ...task });
          }
        }
      }
      rewardedActions = tasksTodo.filter((action) => !action?.verification && !settings.SKIP_TASKS.includes(action.nameId));
      // rewardedActions = rewardedActions.filter((action) => !action.totalCurrencySoftAwarded && !settings.SKIP_TASKS.includes(action.nameId));
      // this.log(`Đã lấy được ${rewardedActions.length} nhiệm vụ`, "success");
      // fs.appendFileSync("t.txt", JSON.stringify(tasksTodo));
      if (rewardedActions.length == 0) {
        return this.log(`There are no tasks to perform`, "warning");
      }
      for (const action of rewardedActions) {
        await sleep(1);
        const nameId = action.nameId;
        const currentTime = new Date();
        let canPerformTask = true;
        let waitTime = null;

        if (userInfo.rewardedActions && userInfo.rewardedActions[nameId]) {
          const lastClaimTime = new Date(userInfo.rewardedActions[nameId].claimDateTime);

          if (nameId === "SeveralHourlsReward") {
            const nextAvailableTime = new Date(lastClaimTime.getTime() + 6 * 60 * 60 * 1000);
            if (currentTime < nextAvailableTime) {
              canPerformTask = false;
              waitTime = nextAvailableTime;
            }
          } else if (nameId === "SeveralHourlsRewardedAdTask" || nameId === "SeveralHourlsRewardedAdTask2") {
            const nextAvailableTime = new Date(lastClaimTime.getTime() + 6 * 60 * 1000);
            if (currentTime < nextAvailableTime) {
              canPerformTask = false;
              waitTime = nextAvailableTime;
            }
          } else if (userInfo.rewardedActions[nameId].claimDateTime) {
            canPerformTask = false;
          }
        }

        if (!canPerformTask) {
          if (waitTime) {
            const waitMinutes = Math.ceil((waitTime - currentTime) / (60 * 1000));
            this.log(`Need to wait ${waitMinutes} minutes to continue doing task ${nameId}`, "info");
            } else {
            this.log(`Task ${nameId} has been completed before`, "info");
          }
          continue;
        }
        if (nameId === "SeveralHourlsRewardedAdTask" || nameId === "SeveralHourlsRewardedAdTask2") {
          const providerId = nameId === "SeveralHourlsRewardedAdTask" ? "adsgram" : "onclicka";
          await this.handleAdTask(nameId, providerId);
        } else {
          try {
            const clickResponse = await this.completeTask(nameId);
            // console.log(clickResponse);
            this.log(`Doing task ${nameId.yellow} | status: ${`pending`.yellow}`);
} catch (clickError) {
this.log(`Error while doing task ${nameId}: ${clickError.message}`, "error");
if (clickError.response) {
this.log(`Error details: ${JSON.stringify(clickError.response.data)}`, "error");
            }
            continue;
          }

          if (action.secondsToAllowClaim > 0) {
            this.log(`Đợi ${action.secondsToAllowClaim} giây...`);
            await sleep(action.secondsToAllowClaim);
          }

          try {
            const claimResponse = await this.claimTask(nameId);
            if (claimResponse.success && claimResponse.data) {
              const result = claimResponse.data;
              const reward = result.prizeGotten;
              this.log(`Completed quest ${nameId} successfully | Reward: ${reward || JSON.stringify(result)}`, "success");
} else {
this.log(`Unable to claim reward for ${nameId} | ${JSON.stringify(claimResponse)}`, "error");
}
} catch (claimError) {
this.log(`Error claiming reward for ${nameId}: waiting time still available!`, "warning");
          }
        }

        await sleep(1);
      }
    } catch (error) {
      this.log(`Error while performing tasks: ${error.message}`, "error");
if (error.response) {
this.log(`Error details: ${JSON.stringify(error.response.data)}`, "error");
      }
    }
  }

  async handleAdTask(nameId, providerId) {
    try {
      await this.clickAds(nameId);
      this.log(`Clicked ad task ${nameId}`, "success");
await new Promise((resolve) => setTimeout(resolve, 2000));
await this.watchAd({ providerId });
this.log(`Confirmed viewing ad for ${nameId}`, "success");
await new Promise((resolve) => setTimeout(resolve, 2000));
this.log(`Sending request for reward for ad task${nameId}...`, "info");
      const claimResponse = await this.claimTask(nameId);

      if (claimResponse.success) {
        const result = claimResponse.data;
        const reward = result.prizeGotten;
        this.log(`Successfully completed advertising task ${nameId} | Reward: ${reward}`, "success");
} else {
this.log(`Unable to claim reward for advertising task ${nameId}. Status code: ${claimResponse.status}`, "error");
}
} catch (error) {
this.log(`Error processing advertising task ${nameId}: timeout still exists!`, "error");
    }
  }

  async checkProxyIP(proxy) {
    try {
      const proxyAgent = new HttpsProxyAgent(proxy);
      const response = await axios.get("https://api.ipify.org?format=json", {
        httpsAgent: proxyAgent,
        timeout: 10000,
      });
      if (response.status === 200) {
        return response.data.ip;
      } else {
        throw new Error(`Could not check proxy IP. Status code: ${response.status}`);
}
} catch (error) {
throw new Error(`Error when checking proxy IP: ${error.message}`);
    }
  }

  async getValidToken() {
    const userId = this.session_name;
    const existingToken = this.token;
    let loginResult = null;
    const isExp = isTokenExpired(existingToken);
    if (existingToken && !isExp) {
      this.log("Using valid token", "success");
      return existingToken;
    } else {
      this.log("Token not found or expired, login...", "warning");
      loginResult = await this.loginByTelegram();
      if (loginResult.success) {
        this.log("Login successful!", "success");
saveToken(userId, loginResult.token);
return loginResult.token;
} else {
this.log(`Login failed!${loginResult.status || loginResult.error}`, "error");
        return null;
      }
    }
  }

  async runAccount() {
    const tgData = this.queryId;
    const userData = JSON.parse(decodeURIComponent(tgData.split("user=")[1].split("&")[0]));
    const firstName = userData.first_name;
    const lastName = userData.last_name || "";
    this.session_name = userData.id;
    this.token = this.tokens[this.session_name];
    this.set_headers();
    if (settings.USE_PROXY) {
      try {
        this.proxyIP = await this.checkProxyIP(this.proxy);
      } catch (error) {
        this.log(`Cannot check proxy IP: ${error.message}`, "warning");
        return;
      }
    }
    const timesleep = getRandomNumber(settings.DELAY_START_BOT[0], settings.DELAY_START_BOT[1]);
    console.log(`=========Account ${this.accountIndex + 1}| ${firstName + " " + lastName} | ${settings.USE_PROXY ? this.proxyIP : "No proxy"} | Starts in ${timesleep} seconds...`.green);
    await sleep(timesleep);

    const token = await this.getValidToken();
    if (!token) {
      this.log("Token not found or token expired...skiping", "error");
      return;
    }
    this.token = token;

    try {
      const userInfoResult = await this.getUserData();
      // const configResult = await this.getConfig();
      if (userInfoResult.success) {
        const userInfo = userInfoResult.data;
        this.log(
          `Amount bonkiers: ${userInfo?.boinkers?.completedBoinkers} | Shit Balance: ${userInfo?.currencyCrypto || 0} | Spin: ${userInfo.gamesEnergy.slotMachine.energy} | Level: ${
            userInfo.boinkers.currentBoinkerProgression.level
          } | Coin Balance: ${userInfo.currencySoft || 0}`,
          "info"
        );
        const currentTime = DateTime.now();
        const lastClaimedTime = userInfo.boinkers?.booster?.x2?.lastTimeFreeOptionClaimed ? DateTime.fromISO(userInfo.boinkers.booster.x2.lastTimeFreeOptionClaimed) : null;

        if (!lastClaimedTime || currentTime > lastClaimedTime.plus({ hours: 2, minutes: 5 })) {
          const boosterResult = await this.claimBooster(userInfo.gamesEnergy.slotMachine.energy);
          if (!boosterResult.success) {
            this.log(`Cannot claim booster: ${boosterResult.error}`, "error");
}
} else {
const nextBoosterTime = lastClaimedTime.plus({ hours: 2, minutes: 5 });
this.log(`Time to buy next boosts: ${nextBoosterTime.toLocaleString(DateTime.DATETIME_MED)}`, "info");
        }

        const spinuser = await this.getUserData();
        const spinUser = spinuser.data;
        for (const type of ["slotMachine"]) {
          const spins = spinUser.gamesEnergy[type].energy;
          if (spins > 0) {
            this.log(`Start spinning ${type} with ${spins} spins`, "yellow");
await this.spinSlotMachine(type, spins);
} else {
this.log("No spins", "warning");
          }
        }

        await this.performRewardedActions();

        await this.handleUpgradeBoinker();
        // let upgradeSuccess = true;
        // while (upgradeSuccess) {
        //   upgradeSuccess = upgradeResult.success;
        // }
      } else {
        return this.log(`Unable to get user info! ${JSON.stringify(userInfoResult)}`, "error");
}
} catch (error) {
this.log(`Error processing account: ${error.message}`, "error");
    }

    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
}

async function runWorker(workerData) {
  const { queryId, accountIndex, proxy, hasIDAPI, tokens } = workerData;
  const to = new Boink(queryId, accountIndex, proxy, hasIDAPI, tokens);
  try {
    await Promise.race([to.runAccount(), new Promise((_, reject) => setTimeout(() => reject(new Error("Timeout")), 24 * 60 * 60 * 1000))]);
    parentPort.postMessage({
      accountIndex,
    });
  } catch (error) {
    parentPort.postMessage({ accountIndex, error: error.message });
  } finally {
    if (!isMainThread) {
      parentPort.postMessage("taskComplete");
    }
  }
}

async function main() {
  const queryIds = loadData("data.txt");
  const proxies = loadData("proxy.txt");
  const tokens = require("./token.json");

  // const agents = #load_session_data();
  //   const wallets = loadData("wallets.txt");

  if (queryIds.length > proxies.length && settings.USE_PROXY) {
    console.log("The number of proxies and data must be equal..".red);
    console.log(`Data: ${queryIds.length}`);
    console.log(`Proxy: ${proxies.length}`);
    process.exit(1);
  }
  console.log(colors.yellow("Join Telegram Channel (https://t.me/D4rkCipherX)"));

  if (!settings.USE_PROXY) {
    console.log(`You are running bot without proxies, enable use proxy by key USE_PROXY in file .env`.yellow);
  }
  let maxThreads = settings.USE_PROXY ? settings.MAX_THEADS : settings.MAX_THEADS_NO_PROXY;

  const { endpoint: hasIDAPI, message } = await checkBaseUrl();
  if (!hasIDAPI) return console.log(`API ID not found, try again later!`.red);
  console.log(`${message}`.yellow);
  // process.exit();
  queryIds.map((val, i) => new Boink(val, i, proxies[i], hasIDAPI, tokens).createUserAgent());

  await sleep(1);
  while (true) {
    let currentIndex = 0;
    const errors = [];

    while (currentIndex < queryIds.length) {
      const workerPromises = [];
      const batchSize = Math.min(maxThreads, queryIds.length - currentIndex);
      for (let i = 0; i < batchSize; i++) {
        const worker = new Worker(__filename, {
          workerData: {
            hasIDAPI,
            queryId: queryIds[currentIndex],
            accountIndex: currentIndex,
            proxy: proxies[currentIndex % proxies.length],
            tokens,
          },
        });

        workerPromises.push(
          new Promise((resolve) => {
            worker.on("message", (message) => {
              if (message === "taskComplete") {
                worker.terminate();
              }
              // console.log(message);
              resolve();
            });
            worker.on("error", (error) => {
              console.log(`Worker error for account ${currentIndex}: ${error.message}`);
worker.terminate();
});
worker.on("exit", (code) => {
worker.terminate();
if (code !== 0) {
errors.push(`Worker for account ${currentIndex} exited with code: ${code}`);
              }
              resolve();
            });
          })
        );

        currentIndex++;
      }

      await Promise.all(workerPromises);

      if (errors.length > 0) {
        errors.length = 0;
      }

      if (currentIndex < queryIds.length) {
        await new Promise((resolve) => setTimeout(resolve, 3000));
      }
    }
    await sleep(3);
    console.log(`=============Complete all accounts | Wait ${settings.TIME_SLEEP} minutes=============`.magenta);
    await sleep(settings.TIME_SLEEP * 60);
  }
}

if (isMainThread) {
  main().catch((error) => {
    console.log("It's a mistake:", error);
    process.exit(1);
  });
} else {
  runWorker(workerData);
}
