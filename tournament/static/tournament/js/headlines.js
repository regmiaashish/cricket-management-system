document.addEventListener("DOMContentLoaded", function () {
  const apiKey = '13e8ddd1992b43259053cc0f7f706cc7';  // Replace with your News API key
  const apiUrl = `https://newsapi.org/v2/top-headlines?category=sports&q=cricket&apiKey=${apiKey}`;

  fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
          if (data && data.articles) {
              const headlines = data.articles.map(article => article.title);
              initTypewriter(headlines);
          } else {
              console.error('No articles found or failed to fetch data:', data);
          }
      })
      .catch(error => console.error('Error fetching headlines:', error));
});

function initTypewriter(headlines) {
  const typewriterElement = document.querySelector('.typewrite');
  const typewriterData = JSON.stringify(headlines);
  typewriterElement.setAttribute('data-type', typewriterData);
  startTypewriterEffect();
}

function startTypewriterEffect() {
  const elements = document.querySelectorAll('.typewrite');
  elements.forEach(function (element) {
      const toRotate = JSON.parse(element.getAttribute('data-type'));
      const period = element.getAttribute('data-period');
      let loopNum = 0;
      let txt = '';
      let isDeleting = false;

      function tick() {
          const i = loopNum % toRotate.length;
          const fullTxt = toRotate[i];

          if (isDeleting) {
              txt = fullTxt.substring(0, txt.length - 1);
          } else {
              txt = fullTxt.substring(0, txt.length + 1);
          }

          element.querySelector('.wrap').innerHTML = txt;

          let delta = 200 - Math.random() * 100;
          if (isDeleting) delta /= 2;

          if (!isDeleting && txt === fullTxt) {
              delta = period;
              isDeleting = true;
          } else if (isDeleting && txt === '') {
              isDeleting = false;
              loopNum++;
              delta = 500;
          }

          setTimeout(tick, delta);
      }

      tick();
  });
}
