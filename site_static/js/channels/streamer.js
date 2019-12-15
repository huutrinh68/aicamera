$(document).ready(function(){
    var loc = window.location;

	var wsStart = 'ws://';
	if (loc.protocol == 'https:'){
		wsStart = 'wss://';
	}

	var endpoint = wsStart + loc.host + '/streamer'
	var socket = new ReconnectingWebSocket(endpoint);
    
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
        
    navigator.getUserMedia = navigator.getUserMedia 
	|| navigator.webkitGetUserMedia 
	|| window.navigator.mozGetUserMedia;

	window.URL = window.URL || window.webkitURL;
	var video = document.getElementById("video");
	// const img = document.getElementById("img");
	
	var constraints = {
      audio: false,
      video: true,
	};
	
	navigator.mediaDevices.getUserMedia(constraints)
	.then(function (stream) {
        video.srcObject = stream;
        video.onloadedmetadata = function (e) {
          video.play();
        };
	})
	.catch(function (err) {
        alert(err.name + ": " + err.message);
	});
	
    socket.onmessage = function(e){
        console.log(`Connected to client ${endpoint}`);
        json_data = JSON.parse(e.data);
        console.log(json_data[0].box)
        ctx.beginPath();
        ctx.lineWidth = "4";
        ctx.strokeStyle = "green";
        ctx.rect(json_data.box);
        ctx.stroke();
    };


    const getFrame = () => {
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        const data = canvas.toDataURL('image/png', 1.0);
        return data;
    }
    const FPS = 30;
	socket.onopen = function(e){
        console.log(`connected to server ${endpoint}`)
        setInterval(() => {
            socket.send(getFrame());
        }, 1000 / FPS);
        console.log('open', e);
    };

    socket.onerror = function(e){
        console.log('error', e)
    };

    socket.onclose = function(e){
        console.log('close', e)
    };
});

