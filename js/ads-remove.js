f = document.querySelector("#ads");
c = f.innerHTML;
if(c.includes("           <!--[ADS]-->")){
	f.innerHTML = "<span class='red'>There are no posts, posted by the admin.";
}