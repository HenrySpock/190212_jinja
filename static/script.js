console.log('script.js checking in')

document.addEventListener("DOMContentLoaded", function() {
    const story1Form = document.getElementById('story1-form');
    const story2Form = document.getElementById('story2-form');
    story1Form.style.display = 'none';
    story2Form.style.display = 'none';
  
    document.getElementById("story1-btn").addEventListener("click", function() {
      document.getElementById("story-id").value = "story1";
      showForm("story1");
    });
  
    document.getElementById("story2-btn").addEventListener("click", function() {
      document.getElementById("story-id").value = "story2";
      showForm("story2");
    });
  });
  
  function showForm(storyId) {
    document.querySelectorAll('form').forEach(form => form.style.display = "none");
    const formId = storyId + '-form';
    document.getElementById(formId).style.display = "block";
  }
  
  const story1Btn = document.getElementById('story1-btn');
  const story2Btn = document.getElementById('story2-btn');
  const story1Form = document.getElementById('story1-form');
  const story2Form = document.getElementById('story2-form');

  document.getElementById("story1-btn").addEventListener("click", function() {
    showForm("story1");
  });
  
  document.getElementById("story2-btn").addEventListener("click", function() {
    showForm("story2");
  });
