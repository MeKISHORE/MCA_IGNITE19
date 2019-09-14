
$(document).ready(function(){

        // console.clear();
            class Star {
          constructor() {
            this.position = {
              x: random_range(-(star_count / depth), star_count / depth),
              y: random_range(-(star_count / depth), star_count / depth),
              z: random_range(1, depth) };

            this.speed = 75;
            this.life = 0;
          }}


        const c = document.getElementById('c'),
        $ = c.getContext('2d');

        let w = c.width = innerWidth,
        h = c.height = innerHeight,
        stars = [],
        star_count = 500,
        depth = 20;

        const init = () => {
          for (let i = 0; i < star_count; i++) {
            stars.push(new Star());
          }
          loop();
        };

        const resize = () => {
          w = c.width = innerWidth;
          h = c.height = innerHeight;
        };

        const stage = (background, width, height) => {
          $.fillStyle = background;
          $.fillRect(0, 0, width, height);
        };

        const random_range = (min, max) => {
          return ~~(Math.random() * (max - min)) + min;
        };

        const draw = () => {
          stage('rgba(20, 20, 20, 1)', w, h);
          for (let i = 0; i < stars.length; i++) {
            let s = stars[i],
            k = stars.length / 4 / s.position.z,
            px = s.position.x * k + w / 2,
            py = s.position.y * k + h / 2;
            if (px >= 0 && px <= w && py >= 0 && py <= h) {
              let size = (1 - s.position.z / (stars.length / 8)) * 2;
              $.fillStyle = 'rgba(255, 255, 255, 1)';
              if (s.life < 1) {
                $.fillStyle = 'rgba(255, 255, 255, ' + s.life + ')';
                s.life += s.speed / 10000;
              }
              $.beginPath();
              $.arc(px, py, size, 0, Math.PI * 2);
              $.fill();
            }
            if (s.position.z <= 0) {
              stars[i] = new Star();
            }
            s.position.z -= s.speed / 1000;
          }
        };

        const loop = () => {
          draw();
          requestAnimationFrame(loop);
        };

        window.onresize = resize;

        init();


});
