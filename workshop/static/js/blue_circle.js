var svg = document.getElementById('circles');
var groups = svg.children;

var masterTL = new TimelineMax({ paused: true });

for(var i = 0; i < groups.length; i++) {
	var tl = new TimelineMax({ repeat: -1 });
	var options = {
		transformOrigin: '50% 50%',
		rotation: 360,
		ease: SlowMo.ease.config(.9, .6)
	};
	tl.to(groups[i], rndBetween(5, 30), options);
	masterTL.add(tl, Math.random());
};

masterTL.play();

svg.addEventListener('mouseover', function() {
	TweenLite.to(masterTL, .5, { timeScale: .25 });
});

svg.addEventListener('mouseout', function() {
	TweenLite.to(masterTL, .5, { timeScale: 1 });
});

function rndBetween(min, max) {
	return Math.random() * (max - min) + min;
};



function show(){

	document.getElementById('techcircle').style.display="block";
}