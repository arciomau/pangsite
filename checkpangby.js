function checkpang() {
	var mystr=prompt("Напішыце панграму і націсніце ОК", "Хоць віжуй, дзе яшчэ быў ёлуп-гусар з німфеткаю!").toLowerCase();
	mystr=mystr.replace(/[^\а\б\в\г\д\е\ё\ж\з\і\й\к\л\м\н\о\п\р\с\т\у\ў\ф\х\ц\ч\ш\ы\ь\э\ю\я]/g,"");
	var charset="абвгдеёжзійклмнопрстуўфхцчшыьэюя";

	function splitstr(userstring) {
   		var regexp=/.[\u0300-\u036F]*/g;
    	var els,resm=[];
    	while (els=regexp.exec(userstring))
        	resm.push(els[0]);
    	return resm;
	}

	var nodups=function(myarr) {
		var arrayunique=[], len=myarr.length, isfnd, i, j;
		for (i=0; i<len; i++) {
			isfnd = false;
                        for (j=0; j<arrayunique.length; j++) {
				if (myarr[i]===arrayunique[j]) {
					isfnd = true;
					break;
				}
			}
		if (!isfnd) arrayunique.push(myarr[i]);
		}
        return arrayunique;
	}

	function getdiff(first, second) {
            var nonunique=[],diff=[], i;
            for (i=0; i<second.length; i++)
      		nonunique[second[i]]=true;
            for (i=0; i<first.length; i++)
      		if (!nonunique[first[i]])
          		diff.push(first[i]);
         return diff;
	}

	arr=splitstr(mystr);
	var arrlen=arr.length;
	arr=nodups(arr).sort(function (i, j) {return i.localeCompare(j);});

	if (mystr) {
		if (arr.join("")===charset) {
			alert("Гэта панграма! ("+String(arrlen)+" літ.)");
		} else {
			var diff=getdiff(splitstr(charset),arr);
			lendiff=diff.length;
			alert("У радку "+String(arrlen)+" літ. Гэта не панграма!\n"+"Няма "+String(lendiff)+" літ.\n"+diff.join(" "));
		};
	}
	else {
		alert("Памылка! Пусты радок (або небеларускія літары ў радку)");
	}
}