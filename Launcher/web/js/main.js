function changeClass (elem)
{
	var checkClass = elem.className;
	var elementId = elem.id;
	if (checkClass !== "buttonPressed")
		{	
			document.getElementById(elementId).className = "boom";
			setTimeout(function(){
				document.getElementById(elementId).className = "buttonPressed";	
			}, 645);	
			document.getElementById(elementId).innerHTML = "Fired";
			var replace = (elementId).replace('button','');
			var log_window = document.getElementById("log");
			log_window.innerHTML += '<br />' + "Fired Cue: " + (replace);
			log_window.scrollTop = log_window.scrollHeight;
			eel.Fired(elementId);
		}
}

