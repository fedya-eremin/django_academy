var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.3.min.js'; 
document.getElementsByTagName('head')[0].appendChild(script);

const a = document.getElementsByTagName("footer")[0]
	.appendChild(document.createElement("div"));

const serverTime = parseInt(document.getElementById("hidden-time").innerHTML) // some stupid #$%&

const currentTime = () => {
	if (Math.abs(serverTime*1000-Date.now())>24*60*60*1000) {
		var date = serverTime
	}else {
		var date = new Intl.DateTimeFormat().resolvedOptions().timeZone;
	}
	a.innerHTML = Date(date);
}
setInterval(currentTime, 1000);


$(".gallery-box").children(".img-box").add("button")
