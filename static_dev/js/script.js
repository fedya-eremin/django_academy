
const a = document.getElementsByTagName("footer")[0]
	.appendChild(document.createElement("p"));
currentTime = () => {
	a.innerHTML = Date(Date(Intl.DateTimeFormat().resolvedOptions().timeZone));
}

setInterval(currentTime, 1000);


