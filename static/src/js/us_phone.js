odoo.define('purchase_order_enhancement.us_phone', function(require) {
    'use strict';
    
    var field_registry = require('web.field_registry');
    var FieldChar = require('web.basic_fields').FieldChar;

    function formatPhoneNumber(phoneNumberString) {
        var cleaned = ('' + phoneNumberString).replace(/\D/g, '');
        var match = cleaned.match(/^(1|)?(\d{3})(\d{3})(\d{4})$/);
        if (match) {
          var intlCode = (match[1] ? '+1 ' : '');
          return [intlCode, '(', match[2], ') ', match[3], '-', match[4]].join('');
        }
        return cleaned;
    }

    var UsPhone = FieldChar.extend({
        className: 'o_field_us_phone',

        events: _.extend({}, FieldChar.prototype.events, {
            'keyup': '_onKeyUp',
        }), 

        _onKeyUp: function (e) {
            e.target.value = formatPhoneNumber(e.target.value);
        },
    });

    field_registry.add('us_phone', UsPhone);
    return UsPhone;
});