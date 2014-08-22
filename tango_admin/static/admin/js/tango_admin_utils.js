/* global tango_admin django */

function getMediaQueryName() {
  // Extract media query name from container:after,
  // Where the css left it.
  var mq,
      container = document.body;
  if (container) {
    mq = window.getComputedStyle(container, ':after').getPropertyValue('content');
  }
  return mq;
};


(function($) {
  var mq = getMediaQueryName();

  // On small layouts, hide tabular headers and create placeholder attributes
  if (mq == 'x-small') {
    var $tables = $('.tabular table')
    $tables.find('tbody td').each(function (index) {
      var $this = $(this),
          $theads = $this.closest('table').find('thead th'),
          col = $this.parent().children().index($this),
          $input = $this.find('input[type=text]', 'textarea'),
          $checkbox = $this.find('input[type=checkbox]', 'input[type=radio]'),
          $fileinput = $this.find('input[type=file]')

      if ($input.length > 0 ) {
        $input.attr('placeholder', $theads.eq(col-1).text())
      }
      if ($checkbox.length > 0 ) {
        $checkbox.after($theads.eq(col-1).text())
      }
      if ($fileinput.length > 0 ) {
        $fileinput.before($theads.eq(col-1).text())
      }
    })
  }

  // Apply drag-drop sorting/re-ordering to tabular inlines.
  // NOTE: THIS ONLY WORKS ON TABULAR INLINES.
  var $objectRows = $('div.inline-related tbody tr');
  $objectRows
    .attr('title', 'Drag and drop to re-set order')
    .css('cursor', 'move');

  $('div.inline-group').sortable({
    axis: 'y',
    opacity: 0.7,
    items: 'div.inline-related tbody tr',
    handle: 'td',
    update: function() {
      $('div.inline-related tbody tr').each(function(i) {
          var $this = $(this);
          // only set order if there is an item
          if ($this.find('td.original input:first').val()) {
            $this.find('td.field-order input').val(i + 1);
          }
      });
      $('div.inline-related tbody tr:odd').removeClass('row2').addClass('row1');
      $('div.inline-related tbody tr:even').removeClass('row1').addClass('row2');
    }
  });

  // Textarea counting
  $('textarea[data-counter]').each(function() {
    var max = 140,
        $field = $(this),
        $c = $("<span class='counter'></span>"),
        $help = $('<p class="help"></p>');

    $field.next().after($help.append($c));

    $c.after('  characters remaining')
     .css("padding", "0 3px 0 3px")
     .css("border", "1px solid #ccc");

    function get_remaining() {
        var cur = $field.val().length,
            remaining = max - cur;

        $c.text(remaining.toString());

        if(remaining <= 10) {
            $c.css("background", "#F4F379");
        } else {
            $c.css("background", "none");
        }
    }
    get_remaining();

    $field.keyup(function() {
        get_remaining();
    });
    $("#id_link").change(function() {
      if (this.value.length > 0) {
          $c.text($c.text() - this.value.length);
      }
    });
  });
  // END TEXTAREA COUNTING

  // SIMPLE jump-to-url selectbox
  $(document).on('change', 'select.url-selector', function() {
    'use strict';
    window.location = $(this).val();
  });
})(django.jQuery);

