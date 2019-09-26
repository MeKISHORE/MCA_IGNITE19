$("#chat-label").click(function() {

  $('#live-chat').toggleClass('open-chat');
  $('#chat-label').toggleClass('open-chat-label');
  $('.live-chat-up-arrow').toggleClass('hide-up-arrow');
  $('.live-chat-down-arrow').toggleClass('show-down-arrow');

});