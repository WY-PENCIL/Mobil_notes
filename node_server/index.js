const fs = require("fs");
const express = require("express");
const chalk = require("chalk");

const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
app.use(cors());
const port = 5000;
const ip = "192.168.1.70";

app.get("/", (req, res) => {
  fs.readFile(`./page/inputWords.html`, "utf8", (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    res.send("success");
  });
});
app.post("/addWord", (req, res) => {
    //获取请求参数
    console.log("请求数据",req.body,res.body);
    res.send(JSON.stringify({res:"success",code:200}));
});
app.listen(port, ip, () => {
  console.log(`服务器运行在:${chalk.green("http://" + ip + ":" + port)}`);
});
