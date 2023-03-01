const a = document.getElementsByTagName("footer")[0]
	.appendChild(document.createElement("div"));
const currentTime = () => {
	const date = new Intl.DateTimeFormat().resolvedOptions().timeZone;
	a.innerHTML = Date(date);
}
setInterval(currentTime, 1000);
