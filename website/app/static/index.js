/* Houses async functions to control JSON/chat */
async function add_messages(msg, scroll) {
    if (typeof msg.name !== "undefined") {
      var date = dateNow();
  
      if (typeof msg.time !== "undefined") {
        var n = msg.time;
      } else {
        var n = date;
      }
      var global_name = await load_name();
  
      var content =
        '<div class="container">' +
        '<b style="color:#000" class="right">' +
        msg.name +
        "</b><p>" +
        msg.message +
        '</p><span class="time-right">' +
        n +
        "</span></div>";
      if (global_name == msg.name) {
        content =
          '<div class="container darker">' +
          '<b style="color:#000" class="left">' +
          msg.name +
          "</b><p>" +
          msg.message +
          '</p><span class="time-left">' +
          n +
          "</span></div>";
      }
      // update HTML div
      var messageDiv = document.getElementById("messages");
      messageDiv.innerHTML += content;
    }
  
    if (scroll) {
      scrollSmoothToBottom("messages");
    }
  }
  
  async function load_name() {
    return await fetch("/get_name")
      .then(async function (response) {
        return await response.json();
      })
      .then(function (text) {
        return text["name"];
      });
  }
  
  async function load_messages() {
    return await fetch("/get_messages")
      .then(async function (response) {
        return await response.json();
      })
      .then(function (text) {
        console.log(text);
        return text;
      });
  }
  
  // message size scaling
  $(function () {
    $(".msgs").css({ height: $(window).height() * 0.7 + "px" });
  
    $(window).bind("resize", function () {
      $(".msgs").css({ height: $(window).height() * 0.7 + "px" });
    });
  });
  
  function scrollSmoothToBottom(id) {
    var div = document.getElementById(id);
    $("#" + id).animate(
      {
        scrollTop: div.scrollHeight - div.clientHeight,
      },
      500
    );
  }
  // format message times
  function dateNow() {
    var date = new Date();
    var yyyy = date.getFullYear();
    var dd = date.getDate();
    var mm = date.getMonth() + 1;
  
    if (dd < 10) dd = "0" + dd;
  
    if (mm < 10) mm = "0" + mm;
  
    var cur_day = yyyy + "-" + mm + "-" + dd;
  
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    
    if (hours < 10) hours = "0" + hours;
  
    if (minutes < 10) minutes = "0" + minutes;
  
    if (seconds < 10) seconds = "0" + seconds;
  
    return cur_day + " " + hours + ":" + minutes;
  }
  // connect to server via socket
  var socket = io.connect("http://" + document.domain + ":" + location.port);
  socket.on("connect", async function () {
    var usr_name = await load_name();
    if (usr_name != "") {
      socket.emit("event", {
        message: usr_name + " has connected to the server",
        connect: true,
      });
    }
    var form = $("form#msgForm").on("submit", async function (e) {
      e.preventDefault();
  
      // get input from message box
      let msg_input = document.getElementById("msg");
      let user_input = msg_input.value;
      let user_name = await load_name();
  
      // clear msg box value
      msg_input.value = "";
  
      // send message to other users
      socket.emit("event", {
        message: user_input,
        name: user_name,
      });
    });
  });
  // disconnect from server
  socket.on("disconnect", async function (msg) {
    var usr_name = await load_name();
    socket.emit("event", {
      message: usr_name + " has left the server",
    });
  });
  socket.on("message response", function (msg) {
    add_messages(msg, true);
  });
  
  // load messages, then if msgs scroll
  window.onload = async function () {
    var msgs = await load_messages();
    for (i = 0; i < msgs.length; i++) {
      scroll = false;
      if (i == msgs.length - 1) {
        scroll = true;
      }
      add_messages(msgs[i], scroll);
    }
    // hiding login/out messages from the chat
    let name = await load_name();
    if (name != "") {
      $("#login").hide();
    } else {
      $("#logout").hide();
    }
  };
  