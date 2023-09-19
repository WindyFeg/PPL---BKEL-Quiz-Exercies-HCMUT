/*
YUI 3.17.2 (build 9c3c78e)
Copyright 2014 Yahoo! Inc. All rights reserved.
Licensed under the BSD License.
http://yuilibrary.com/license/
*/

YUI.add('event-mousewheel', function (Y, NAME) {

/**
 * Adds mousewheel event support
 * @module event
 * @submodule event-mousewheel
 */
var DOM_MOUSE_SCROLL = 'DOMMouseScroll',
    fixArgs = function(args) {
        var a = Y.Array(args, 0, true), target;
        if (Y.UA.gecko) {
            a[0] = DOM_MOUSE_SCROLL;
            target = Y.config.win;
        } else {
            target = Y.config.doc;
        }

        if (a.length < 3) {
            a[2] = target;
        } else {
            a.splice(2, 0, target);
        }

        return a;
    };

/**
 * Mousewheel event.  This listener is automatically attached to the
 * correct target, so one should not be supplied.  Mouse wheel
 * direction and velocity is stored in the 'wheelDelta' field.
 * @event mousewheel
 * @param type {string} 'mousewheel'
 * @param fn {function} the callback to execute
 * @param context optional context object
 * @param args 0..n additional arguments to provide to the listener.
 * @return {EventHandle} the detach handle
 * @for YUI
 */
Y.Env.evt.plugins.mousewheel = {
    on: function() {
        return Y.Event._attach(fixArgs(arguments));
    },

    detach: function() {
        return Y.Event.detach.apply(Y.Event, fixArgs(arguments));
    }
};


}, '3.17.2', {"requires": ["node-base"]});
/*
YUI 3.17.2 (build 9c3c78e)
Copyright 2014 Yahoo! Inc. All rights reserved.
Licensed under the BSD License.
http://yuilibrary.com/license/
*/

YUI.add('event-resize', function (Y, NAME) {

/**
 * Adds a window resize event that has its behavior normalized to fire at the
 * end of the resize rather than constantly during the resize.
 * @module event
 * @submodule event-resize
 */


/**
 * Old firefox fires the window resize event once when the resize action
 * finishes, other browsers fire the event periodically during the
 * resize.  This code uses timeout logic to simulate the Firefox
 * behavior in other browsers.
 * @event windowresize
 * @for YUI
 */
Y.Event.define('windowresize', {

    on: (Y.UA.gecko && Y.UA.gecko < 1.91) ?
        function (node, sub, notifier) {
            sub._handle = Y.Event.attach('resize', function (e) {
                notifier.fire(e);
            });
        } :
        function (node, sub, notifier) {
            // interval bumped from 40 to 100ms as of 3.4.1
            var delay = Y.config.windowResizeDelay || 100;

            sub._handle = Y.Event.attach('resize', function (e) {
                if (sub._timer) {
                    sub._timer.cancel();
                }

                sub._timer = Y.later(delay, Y, function () {
                    notifier.fire(e);
                });
            });
        },

    detach: function (node, sub) {
        if (sub._timer) {
            sub._timer.cancel();
        }
        sub._handle.detach();
    }
    // delegate methods not defined because this only works for window
    // subscriptions, so...yeah.
});


}, '3.17.2', {"requires": ["node-base", "event-synthetic"]});
/*
YUI 3.17.2 (build 9c3c78e)
Copyright 2014 Yahoo! Inc. All rights reserved.
Licensed under the BSD License.
http://yuilibrary.com/license/
*/

YUI.add('event-hover', function (Y, NAME) {

/**
 * Adds support for a "hover" event.  The event provides a convenience wrapper
 * for subscribing separately to mouseenter and mouseleave.  The signature for
 * subscribing to the event is</p>
 *
 * <pre><code>node.on("hover", overFn, outFn);
 * node.delegate("hover", overFn, outFn, ".filterSelector");
 * Y.on("hover", overFn, outFn, ".targetSelector");
 * Y.delegate("hover", overFn, outFn, "#container", ".filterSelector");
 * </code></pre>
 *
 * <p>Additionally, for compatibility with a more typical subscription
 * signature, the following are also supported:</p>
 *
 * <pre><code>Y.on("hover", overFn, ".targetSelector", outFn);
 * Y.delegate("hover", overFn, "#container", outFn, ".filterSelector");
 * </code></pre>
 *
 * @module event
 * @submodule event-hover
 */
var isFunction = Y.Lang.isFunction,
    noop = function () {},
    conf = {
        processArgs: function (args) {
            // Y.delegate('hover', over, out, '#container', '.filter')
            // comes in as ['hover', over, out, '#container', '.filter'], but
            // node.delegate('hover', over, out, '.filter')
            // comes in as ['hover', over, containerEl, out, '.filter']
            var i = isFunction(args[2]) ? 2 : 3;

            return (isFunction(args[i])) ? args.splice(i,1)[0] : noop;
        },

        on: function (node, sub, notifier, filter) {
            var args = (sub.args) ? sub.args.slice() : [];

            args.unshift(null);

            sub._detach = node[(filter) ? "delegate" : "on"]({
                mouseenter: function (e) {
                    e.phase = 'over';
                    notifier.fire(e);
                },
                mouseleave: function (e) {
                    var thisObj = sub.context || this;

                    args[0] = e;

                    e.type = 'hover';
                    e.phase = 'out';
                    sub._extra.apply(thisObj, args);
                }
            }, filter);
        },

        detach: function (node, sub, notifier) {
            sub._detach.detach();
        }
    };

conf.delegate = conf.on;
conf.detachDelegate = conf.detach;

Y.Event.define("hover", conf);


}, '3.17.2', {"requires": ["event-mouseenter"]});
/*
YUI 3.17.2 (build 9c3c78e)
Copyright 2014 Yahoo! Inc. All rights reserved.
Licensed under the BSD License.
http://yuilibrary.com/license/
*/

YUI.add('event-touch', function (Y, NAME) {

/**
Adds touch event facade normalization properties (touches, changedTouches, targetTouches etc.) to the DOM event facade. Adds
touch events to the DOM events whitelist.

@example
    YUI().use('event-touch', function (Y) {
        Y.one('#myDiv').on('touchstart', function(e) {
            ...
        });
    });
@module event
@submodule event-touch
 */
var SCALE = "scale",
    ROTATION = "rotation",
    IDENTIFIER = "identifier",
    win = Y.config.win,
    GESTURE_MAP = {};

/**
 * Adds touch event facade normalization properties to the DOM event facade
 *
 * @method _touch
 * @for DOMEventFacade
 * @private
 * @param ev {Event} the DOM event
 * @param currentTarget {HTMLElement} the element the listener was attached to
 * @param wrapper {CustomEvent} the custom event wrapper for this DOM event
 */
Y.DOMEventFacade.prototype._touch = function(e, currentTarget, wrapper) {

    var i,l, etCached, et,touchCache;


    if (e.touches) {

        /**
         * Array of individual touch events for touch points that are still in
         * contact with the touch surface.
         *
         * @property touches
         * @type {DOMEventFacade[]}
         */
        this.touches = [];
        touchCache = {};

        for (i = 0, l = e.touches.length; i < l; ++i) {
            et = e.touches[i];
            touchCache[Y.stamp(et)] = this.touches[i] = new Y.DOMEventFacade(et, currentTarget, wrapper);
        }
    }

    if (e.targetTouches) {

        /**
         * Array of individual touch events still in contact with the touch
         * surface and whose `touchstart` event occurred inside the same taregt
         * element as the current target element.
         *
         * @property targetTouches
         * @type {DOMEventFacade[]}
         */
        this.targetTouches = [];

        for (i = 0, l = e.targetTouches.length; i < l; ++i) {
            et = e.targetTouches[i];
            etCached = touchCache && touchCache[Y.stamp(et, true)];

            this.targetTouches[i] = etCached || new Y.DOMEventFacade(et, currentTarget, wrapper);

        }
    }

    if (e.changedTouches) {

        /**
        An array of event-specific touch events.

        For `touchstart`, the touch points that became active with the current
        event.

        For `touchmove`, the touch points that have changed since the last
        event.

        For `touchend`, the touch points that have been removed from the touch
        surface.

        @property changedTouches
        @type {DOMEventFacade[]}
        **/
        this.changedTouches = [];

        for (i = 0, l = e.changedTouches.length; i < l; ++i) {
            et = e.changedTouches[i];
            etCached = touchCache && touchCache[Y.stamp(et, true)];

            this.changedTouches[i] = etCached || new Y.DOMEventFacade(et, currentTarget, wrapper);

        }
    }

    if (SCALE in e) {
        this[SCALE] = e[SCALE];
    }

    if (ROTATION in e) {
        this[ROTATION] = e[ROTATION];
    }

    if (IDENTIFIER in e) {
        this[IDENTIFIER] = e[IDENTIFIER];
    }
};

//Adding MSPointer events to whitelisted DOM Events. MSPointer event payloads
//have the same properties as mouse events.
if (Y.Node.DOM_EVENTS) {
    Y.mix(Y.Node.DOM_EVENTS, {
        touchstart:1,
        touchmove:1,
        touchend:1,
        touchcancel:1,
        gesturestart:1,
        gesturechange:1,
        gestureend:1,
        MSPointerDown:1,
        MSPointerUp:1,
        MSPointerMove:1,
        MSPointerCancel:1,
        pointerdown:1,
        pointerup:1,
        pointermove:1,
        pointercancel:1
    });
}

//Add properties to Y.EVENT.GESTURE_MAP based on feature detection.
if ((win && ("ontouchstart" in win)) && !(Y.UA.chrome && Y.UA.chrome < 6)) {
    GESTURE_MAP.start = ["touchstart", "mousedown"];
    GESTURE_MAP.end = ["touchend", "mouseup"];
    GESTURE_MAP.move = ["touchmove", "mousemove"];
    GESTURE_MAP.cancel = ["touchcancel", "mousecancel"];
}

else if (win && win.PointerEvent) {
    GESTURE_MAP.start = "pointerdown";
    GESTURE_MAP.end = "pointerup";
    GESTURE_MAP.move = "pointermove";
    GESTURE_MAP.cancel = "pointercancel";
}

else if (win && ("msPointerEnabled" in win.navigator)) {
    GESTURE_MAP.start = "MSPointerDown";
    GESTURE_MAP.end = "MSPointerUp";
    GESTURE_MAP.move = "MSPointerMove";
    GESTURE_MAP.cancel = "MSPointerCancel";
}

else {
    GESTURE_MAP.start = "mousedown";
    GESTURE_MAP.end = "mouseup";
    GESTURE_MAP.move = "mousemove";
    GESTURE_MAP.cancel = "mousecancel";
}

/**
 * A object literal with keys "start", "end", and "move". The value for each key is a
 * string representing the event for that environment. For touch environments, the respective
 * values are "touchstart", "touchend" and "touchmove". Mouse and MSPointer environments are also
 * supported via feature detection.
 *
 * @property _GESTURE_MAP
 * @type Object
 * @static
 */
Y.Event._GESTURE_MAP = GESTURE_MAP;


}, '3.17.2', {"requires": ["node-base"]});
/*
YUI 3.17.2 (build 9c3c78e)
Copyright 2014 Yahoo! Inc. All rights reserved.
Licensed under the BSD License.
http://yuilibrary.com/license/
*/

YUI.add('event-move', function (Y, NAME) {

/**
 * Adds lower level support for "gesturemovestart", "gesturemove" and "gesturemoveend" events, which can be used to create drag/drop
 * interactions which work across touch and mouse input devices. They correspond to "touchstart", "touchmove" and "touchend" on a touch input
 * device, and "mousedown", "mousemove", "mouseup" on a mouse based input device.
 *
 * <p>Documentation for the gesturemove triplet of events can be found on the <a href="../classes/YUI.html#event_gesturemove">YUI</a> global,
 * along with the other supported events.</p>

 @example

     YUI().use('event-move', function (Y) {
         Y.one('#myNode').on('gesturemovestart', function (e) {
         });
         Y.one('#myNode').on('gesturemove', function (e) {
         });
         Y.one('#myNode').on('gesturemoveend', function (e) {
         });
     });

 * @module event-gestures
 * @submodule event-move
 */


 var GESTURE_MAP = Y.Event._GESTURE_MAP,
     EVENT = {
         start: GESTURE_MAP.start,
         end: GESTURE_MAP.end,
         move: GESTURE_MAP.move
     },
    START = "start",
    MOVE = "move",
    END = "end",

    GESTURE_MOVE = "gesture" + MOVE,
    GESTURE_MOVE_END = GESTURE_MOVE + END,
    GESTURE_MOVE_START = GESTURE_MOVE + START,

    _MOVE_START_HANDLE = "_msh",
    _MOVE_HANDLE = "_mh",
    _MOVE_END_HANDLE = "_meh",

    _DEL_MOVE_START_HANDLE = "_dmsh",
    _DEL_MOVE_HANDLE = "_dmh",
    _DEL_MOVE_END_HANDLE = "_dmeh",

    _MOVE_START = "_ms",
    _MOVE = "_m",

    MIN_TIME = "minTime",
    MIN_DISTANCE = "minDistance",
    PREVENT_DEFAULT = "preventDefault",
    BUTTON = "button",
    OWNER_DOCUMENT = "ownerDocument",

    CURRENT_TARGET = "currentTarget",
    TARGET = "target",

    NODE_TYPE = "nodeType",
    SUPPORTS_POINTER = Y.config.win && ("msPointerEnabled" in Y.config.win.navigator),
    MS_TOUCH_ACTION_COUNT = 'msTouchActionCount',
    MS_INIT_TOUCH_ACTION = 'msInitTouchAction',

    _defArgsProcessor = function(se, args, delegate) {
        var iConfig = (delegate) ? 4 : 3,
            config = (args.length > iConfig) ? Y.merge(args.splice(iConfig,1)[0]) : {};

        if (!(PREVENT_DEFAULT in config)) {
            config[PREVENT_DEFAULT] = se.PREVENT_DEFAULT;
        }

        return config;
    },

    _getRoot = function(node, subscriber) {
        return subscriber._extra.root || (node.get(NODE_TYPE) === 9) ? node : node.get(OWNER_DOCUMENT);
    },

    //Checks to see if the node is the document, and if it is, returns the documentElement.
    _checkDocumentElem = function(node) {
        var elem = node.getDOMNode();
        if (node.compareTo(Y.config.doc) && elem.documentElement) {
            return elem.documentElement;
        }
        else {
            return false;
        }
    },

    _normTouchFacade = function(touchFacade, touch, params) {
        touchFacade.pageX = touch.pageX;
        touchFacade.pageY = touch.pageY;
        touchFacade.screenX = touch.screenX;
        touchFacade.screenY = touch.screenY;
        touchFacade.clientX = touch.clientX;
        touchFacade.clientY = touch.clientY;
        touchFacade[TARGET] = touchFacade[TARGET] || touch[TARGET];
        touchFacade[CURRENT_TARGET] = touchFacade[CURRENT_TARGET] || touch[CURRENT_TARGET];

        touchFacade[BUTTON] = (params && params[BUTTON]) || 1; // default to left (left as per vendors, not W3C which is 0)
    },

    /*
    In IE10 touch mode, gestures will not work properly unless the -ms-touch-action CSS property is set to something other than 'auto'. Read http://msdn.microsoft.com/en-us/library/windows/apps/hh767313.aspx for more info. To get around this, we set -ms-touch-action: none which is the same as e.preventDefault() on touch environments. This tells the browser to fire DOM events for all touch events, and not perform any default behavior.

    The user can over-ride this by setting a more lenient -ms-touch-action property on a node (such as pan-x, pan-y, etc.) via CSS when subscribing to the 'gesturemovestart' event.
    */
    _setTouchActions = function (node) {
        var elem = _checkDocumentElem(node) || node.getDOMNode(),
            num = node.getData(MS_TOUCH_ACTION_COUNT);

        //Checks to see if msTouchAction is supported.
        if (SUPPORTS_POINTER) {
            if (!num) {
                num = 0;
                node.setData(MS_INIT_TOUCH_ACTION, elem.style.msTouchAction);
            }
            elem.style.msTouchAction = Y.Event._DEFAULT_TOUCH_ACTION;
            num++;
            node.setData(MS_TOUCH_ACTION_COUNT, num);
        }
    },

    /*
    Resets the element's -ms-touch-action property back to the original value, This is called on detach() and detachDelegate().
    */
    _unsetTouchActions = function (node) {
        var elem = _checkDocumentElem(node) || node.getDOMNode(),
            num = node.getData(MS_TOUCH_ACTION_COUNT),
            initTouchAction = node.getData(MS_INIT_TOUCH_ACTION);

        if (SUPPORTS_POINTER) {
            num--;
            node.setData(MS_TOUCH_ACTION_COUNT, num);
            if (num === 0 && elem.style.msTouchAction !== initTouchAction) {
                elem.style.msTouchAction = initTouchAction;
            }
        }
    },

    _prevent = function(e, preventDefault) {
        if (preventDefault) {
            // preventDefault is a boolean or a function
            if (!preventDefault.call || preventDefault(e)) {
                e.preventDefault();
            }
        }
    },

    define = Y.Event.define;
    Y.Event._DEFAULT_TOUCH_ACTION = 'none';

/**
 * Sets up a "gesturemovestart" event, that is fired on touch devices in response to a single finger "touchstart",
 * and on mouse based devices in response to a "mousedown". The subscriber can specify the minimum time
 * and distance thresholds which should be crossed before the "gesturemovestart" is fired and for the mouse,
 * which button should initiate a "gesturemovestart". This event can also be listened for using node.delegate().
 *
 * <p>It is recommended that you use Y.bind to set up context and additional arguments for your event handler,
 * however if you want to pass the context and arguments as additional signature arguments to on/delegate,
 * you need to provide a null value for the configuration object, e.g: <code>node.on("gesturemovestart", fn, null, context, arg1, arg2, arg3)</code></p>
 *
 * @event gesturemovestart
 * @for YUI
 * @param type {string} "gesturemovestart"
 * @param fn {function} The method the event invokes. It receives the event facade of the underlying DOM event (mousedown or touchstart.touches[0]) which contains position co-ordinates.
 * @param cfg {Object} Optional. An object which specifies:
 *
 * <dl>
 * <dt>minDistance (defaults to 0)</dt>
 * <dd>The minimum distance threshold which should be crossed before the gesturemovestart is fired</dd>
 * <dt>minTime (defaults to 0)</dt>
 * <dd>The minimum time threshold for which the finger/mouse should be help down before the gesturemovestart is fired</dd>
 * <dt>button (no default)</dt>
 * <dd>In the case of a mouse input device, if the event should only be fired for a specific mouse button.</dd>
 * <dt>preventDefault (defaults to false)</dt>
 * <dd>Can be set to true/false to prevent default behavior as soon as the touchstart or mousedown is received (that is before minTime or minDistance thresholds are crossed, and so before the gesturemovestart listener is notified) so that things like text selection and context popups (on touch devices) can be
 * prevented. This property can also be set to a function, which returns true or false, based on the event facade passed to it (for example, DragDrop can determine if the target is a valid handle or not before preventing default).</dd>
 * </dl>
 *
 * @return {EventHandle} the detach handle
 */

define(GESTURE_MOVE_START, {

    on: function (node, subscriber, ce) {

        //Set -ms-touch-action on IE10 and set preventDefault to true
        _setTouchActions(node);

        subscriber[_MOVE_START_HANDLE] = node.on(EVENT[START],
            this._onStart,
            this,
            node,
            subscriber,
            ce);
    },

    delegate : function(node, subscriber, ce, filter) {

        var se = this;

        subscriber[_DEL_MOVE_START_HANDLE] = node.delegate(EVENT[START],
            function(e) {
                se._onStart(e, node, subscriber, ce, true);
            },
            filter);
    },

    detachDelegate : function(node, subscriber, ce, filter) {
        var handle = subscriber[_DEL_MOVE_START_HANDLE];

        if (handle) {
            handle.detach();
            subscriber[_DEL_MOVE_START_HANDLE] = null;
        }

        _unsetTouchActions(node);
    },

    detach: function (node, subscriber, ce) {
        var startHandle = subscriber[_MOVE_START_HANDLE];

        if (startHandle) {
            startHandle.detach();
            subscriber[_MOVE_START_HANDLE] = null;
        }

        _unsetTouchActions(node);
    },

    processArgs : function(args, delegate) {
        var params = _defArgsProcessor(this, args, delegate);

        if (!(MIN_TIME in params)) {
            params[MIN_TIME] = this.MIN_TIME;
        }

        if (!(MIN_DISTANCE in params)) {
            params[MIN_DISTANCE] = this.MIN_DISTANCE;
        }

        return params;
    },

    _onStart : function(e, node, subscriber, ce, delegate) {

        if (delegate) {
            node = e[CURRENT_TARGET];
        }

        var params = subscriber._extra,
            fireStart = true,
            minTime = params[MIN_TIME],
            minDistance = params[MIN_DISTANCE],
            button = params.button,
            preventDefault = params[PREVENT_DEFAULT],
            root = _getRoot(node, subscriber),
            startXY;

        if (e.touches) {
            if (e.touches.length === 1) {
                _normTouchFacade(e, e.touches[0], params);
            } else {
                fireStart = false;
            }
        } else {
            fireStart = (button === undefined) || (button === e.button);
        }


        if (fireStart) {

            _prevent(e, preventDefault);

            if (minTime === 0 || minDistance === 0) {
                this._start(e, node, ce, params);

            } else {

                startXY = [e.pageX, e.pageY];

                if (minTime > 0) {


                    params._ht = Y.later(minTime, this, this._start, [e, node, ce, params]);

                    params._hme = root.on(EVENT[END], Y.bind(function() {
                        this._cancel(params);
                    }, this));
                }

                if (minDistance > 0) {


                    params._hm = root.on(EVENT[MOVE], Y.bind(function(em) {
                        if (Math.abs(em.pageX - startXY[0]) > minDistance || Math.abs(em.pageY - startXY[1]) > minDistance) {
                            this._start(e, node, ce, params);
                        }
                    }, this));
                }
            }
        }
    },

    _cancel : function(params) {
        if (params._ht) {
            params._ht.cancel();
            params._ht = null;
        }
        if (params._hme) {
            params._hme.detach();
            params._hme = null;
        }
        if (params._hm) {
            params._hm.detach();
            params._hm = null;
        }
    },

    _start : function(e, node, ce, params) {

        if (params) {
            this._cancel(params);
        }

        e.type = GESTURE_MOVE_START;


        node.setData(_MOVE_START, e);
        ce.fire(e);
    },

    MIN_TIME : 0,
    MIN_DISTANCE : 0,
    PREVENT_DEFAULT : false
});

/**
 * Sets up a "gesturemove" event, that is fired on touch devices in response to a single finger "touchmove",
 * and on mouse based devices in response to a "mousemove".
 *
 * <p>By default this event is only fired when the same node
 * has received a "gesturemovestart" event. The subscriber can set standAlone to true, in the configuration properties,
 * if they want to listen for this event without an initial "gesturemovestart".</p>
 *
 * <p>By default this event sets up it's internal "touchmove" and "mousemove" DOM listeners on the document element. The subscriber
 * can set the root configuration property, to specify which node to attach DOM listeners to, if different from the document.</p>
 *
 * <p>This event can also be listened for using node.delegate().</p>
 *
 * <p>It is recommended that you use Y.bind to set up context and additional arguments for your event handler,
 * however if you want to pass the context and arguments as additional signature arguments to on/delegate,
 * you need to provide a null value for the configuration object, e.g: <code>node.on("gesturemove", fn, null, context, arg1, arg2, arg3)</code></p>
 *
 * @event gesturemove
 * @for YUI
 * @param type {string} "gesturemove"
 * @param fn {function} The method the event invokes. It receives the event facade of the underlying DOM event (mousemove or touchmove.touches[0]) which contains position co-ordinates.
 * @param cfg {Object} Optional. An object which specifies:
 * <dl>
 * <dt>standAlone (defaults to false)</dt>
 * <dd>true, if the subscriber should be notified even if a "gesturemovestart" has not occured on the same node.</dd>
 * <dt>root (defaults to document)</dt>
 * <dd>The node to which the internal DOM listeners should be attached.</dd>
 * <dt>preventDefault (defaults to false)</dt>
 * <dd>Can be set to true/false to prevent default behavior as soon as the touchmove or mousemove is received. As with gesturemovestart, can also be set to function which returns true/false based on the event facade passed to it.</dd>
 * </dl>
 *
 * @return {EventHandle} the detach handle
 */
define(GESTURE_MOVE, {

    on : function (node, subscriber, ce) {

        _setTouchActions(node);
        var root = _getRoot(node, subscriber, EVENT[MOVE]),

            moveHandle = root.on(EVENT[MOVE],
                this._onMove,
                this,
                node,
                subscriber,
                ce);

        subscriber[_MOVE_HANDLE] = moveHandle;

    },

    delegate : function(node, subscriber, ce, filter) {

        var se = this;

        subscriber[_DEL_MOVE_HANDLE] = node.delegate(EVENT[MOVE],
            function(e) {
                se._onMove(e, node, subscriber, ce, true);
            },
            filter);
    },

    detach : function (node, subscriber, ce) {
        var moveHandle = subscriber[_MOVE_HANDLE];

        if (moveHandle) {
            moveHandle.detach();
            subscriber[_MOVE_HANDLE] = null;
        }

        _unsetTouchActions(node);
    },

    detachDelegate : function(node, subscriber, ce, filter) {
        var handle = subscriber[_DEL_MOVE_HANDLE];

        if (handle) {
            handle.detach();
            subscriber[_DEL_MOVE_HANDLE] = null;
        }

        _unsetTouchActions(node);

    },

    processArgs : function(args, delegate) {
        return _defArgsProcessor(this, args, delegate);
    },

    _onMove : function(e, node, subscriber, ce, delegate) {

        if (delegate) {
            node = e[CURRENT_TARGET];
        }

        var fireMove = subscriber._extra.standAlone || node.getData(_MOVE_START),
            preventDefault = subscriber._extra.preventDefault;


        if (fireMove) {

            if (e.touches) {
                if (e.touches.length === 1) {
                    _normTouchFacade(e, e.touches[0]);
                } else {
                    fireMove = false;
                }
            }

            if (fireMove) {

                _prevent(e, preventDefault);


                e.type = GESTURE_MOVE;
                ce.fire(e);
            }
        }
    },

    PREVENT_DEFAULT : false
});

/**
 * Sets up a "gesturemoveend" event, that is fired on touch devices in response to a single finger "touchend",
 * and on mouse based devices in response to a "mouseup".
 *
 * <p>By default this event is only fired when the same node
 * has received a "gesturemove" or "gesturemovestart" event. The subscriber can set standAlone to true, in the configuration properties,
 * if they want to listen for this event without a preceding "gesturemovestart" or "gesturemove".</p>
 *
 * <p>By default this event sets up it's internal "touchend" and "mouseup" DOM listeners on the document element. The subscriber
 * can set the root configuration property, to specify which node to attach DOM listeners to, if different from the document.</p>
 *
 * <p>This event can also be listened for using node.delegate().</p>
 *
 * <p>It is recommended that you use Y.bind to set up context and additional arguments for your event handler,
 * however if you want to pass the context and arguments as additional signature arguments to on/delegate,
 * you need to provide a null value for the configuration object, e.g: <code>node.on("gesturemoveend", fn, null, context, arg1, arg2, arg3)</code></p>
 *
 *
 * @event gesturemoveend
 * @for YUI
 * @param type {string} "gesturemoveend"
 * @param fn {function} The method the event invokes. It receives the event facade of the underlying DOM event (mouseup or touchend.changedTouches[0]).
 * @param cfg {Object} Optional. An object which specifies:
 * <dl>
 * <dt>standAlone (defaults to false)</dt>
 * <dd>true, if the subscriber should be notified even if a "gesturemovestart" or "gesturemove" has not occured on the same node.</dd>
 * <dt>root (defaults to document)</dt>
 * <dd>The node to which the internal DOM listeners should be attached.</dd>
 * <dt>preventDefault (defaults to false)</dt>
 * <dd>Can be set to true/false to prevent default behavior as soon as the touchend or mouseup is received. As with gesturemovestart, can also be set to function which returns true/false based on the event facade passed to it.</dd>
 * </dl>
 *
 * @return {EventHandle} the detach handle
 */
define(GESTURE_MOVE_END, {

    on : function (node, subscriber, ce) {
        _setTouchActions(node);
        var root = _getRoot(node, subscriber),

            endHandle = root.on(EVENT[END],
                this._onEnd,
                this,
                node,
                subscriber,
                ce);

        subscriber[_MOVE_END_HANDLE] = endHandle;
    },

    delegate : function(node, subscriber, ce, filter) {

        var se = this;

        subscriber[_DEL_MOVE_END_HANDLE] = node.delegate(EVENT[END],
            function(e) {
                se._onEnd(e, node, subscriber, ce, true);
            },
            filter);
    },

    detachDelegate : function(node, subscriber, ce, filter) {
        var handle = subscriber[_DEL_MOVE_END_HANDLE];

        if (handle) {
            handle.detach();
            subscriber[_DEL_MOVE_END_HANDLE] = null;
        }

        _unsetTouchActions(node);

    },

    detach : function (node, subscriber, ce) {
        var endHandle = subscriber[_MOVE_END_HANDLE];

        if (endHandle) {
            endHandle.detach();
            subscriber[_MOVE_END_HANDLE] = null;
        }

        _unsetTouchActions(node);
    },

    processArgs : function(args, delegate) {
        return _defArgsProcessor(this, args, delegate);
    },

    _onEnd : function(e, node, subscriber, ce, delegate) {

        if (delegate) {
            node = e[CURRENT_TARGET];
        }

        var fireMoveEnd = subscriber._extra.standAlone || node.getData(_MOVE) || node.getData(_MOVE_START),
            preventDefault = subscriber._extra.preventDefault;

        if (fireMoveEnd) {

            if (e.changedTouches) {
                if (e.changedTouches.length === 1) {
                    _normTouchFacade(e, e.changedTouches[0]);
                } else {
                    fireMoveEnd = false;
                }
            }

            if (fireMoveEnd) {

                _prevent(e, preventDefault);

                e.type = GESTURE_MOVE_END;
                ce.fire(e);

                node.clearData(_MOVE_START);
                node.clearData(_MOVE);
            }
        }
    },

    PREVENT_DEFAULT : false
});


}, '3.17.2', {"requires": ["node-base", "event-touch", "event-synthetic"]});
/*
YUI 3.17.2 (build 9c3c78e)
Copyright 2014 Yahoo! Inc. All rights reserved.
Licensed under the BSD License.
http://yuilibrary.com/license/
*/

YUI.add('event-flick', function (Y, NAME) {

/**
 * The gestures module provides gesture events such as "flick", which normalize user interactions
 * across touch and mouse or pointer based input devices. This layer can be used by application developers
 * to build input device agnostic components which behave the same in response to either touch or mouse based
 * interaction.
 *
 * <p>Documentation for events added by this module can be found in the event document for the <a href="../classes/YUI.html#events">YUI</a> global.</p>
 *
 *
 @example

     YUI().use('event-flick', function (Y) {
         Y.one('#myNode').on('flick', function (e) {
         });
     });

 *
 * @module event-gestures
 */

/**
 * Adds support for a "flick" event, which is fired at the end of a touch or mouse based flick gesture, and provides
 * velocity of the flick, along with distance and time information.
 *
 * <p>Documentation for the flick event can be found on the <a href="../classes/YUI.html#event_flick">YUI</a> global,
 * along with the other supported events.</p>
 *
 * @module event-gestures
 * @submodule event-flick
 */
var GESTURE_MAP = Y.Event._GESTURE_MAP,
    EVENT = {
        start: GESTURE_MAP.start,
        end: GESTURE_MAP.end,
        move: GESTURE_MAP.move
    },
    START = "start",
    END = "end",
    MOVE = "move",

    OWNER_DOCUMENT = "ownerDocument",
    MIN_VELOCITY = "minVelocity",
    MIN_DISTANCE = "minDistance",
    PREVENT_DEFAULT = "preventDefault",

    _FLICK_START = "_fs",
    _FLICK_START_HANDLE = "_fsh",
    _FLICK_END_HANDLE = "_feh",
    _FLICK_MOVE_HANDLE = "_fmh",

    NODE_TYPE = "nodeType";

/**
 * Sets up a "flick" event, that is fired whenever the user initiates a flick gesture on the node
 * where the listener is attached. The subscriber can specify a minimum distance or velocity for
 * which the event is to be fired. The subscriber can also specify if there is a particular axis which
 * they are interested in - "x" or "y". If no axis is specified, the axis along which there was most distance
 * covered is used.
 *
 * <p>It is recommended that you use Y.bind to set up context and additional arguments for your event handler,
 * however if you want to pass the context and arguments as additional signature arguments to "on",
 * you need to provide a null value for the configuration object, e.g: <code>node.on("flick", fn, null, context, arg1, arg2, arg3)</code></p>
 *
 * @event flick
 * @for YUI
 * @param type {string} "flick"
 * @param fn {function} The method the event invokes. It receives an event facade with an e.flick object containing the flick related properties: e.flick.time, e.flick.distance, e.flick.velocity and e.flick.axis, e.flick.start.
 * @param cfg {Object} Optional. An object which specifies any of the following:
 * <dl>
 * <dt>minDistance (in pixels, defaults to 10)</dt>
 * <dd>The minimum distance between start and end points, which would qualify the gesture as a flick.</dd>
 * <dt>minVelocity (in pixels/ms, defaults to 0)</dt>
 * <dd>The minimum velocity which would qualify the gesture as a flick.</dd>
 * <dt>preventDefault (defaults to false)</dt>
 * <dd>Can be set to true/false to prevent default behavior as soon as the touchstart/touchend or mousedown/mouseup is received so that things like scrolling or text selection can be
 * prevented. This property can also be set to a function, which returns true or false, based on the event facade passed to it.</dd>
 * <dt>axis (no default)</dt>
 * <dd>Can be set to "x" or "y" if you want to constrain the flick velocity and distance to a single axis. If not
 * defined, the axis along which the maximum distance was covered is used.</dd>
 * </dl>
 * @return {EventHandle} the detach handle
 */

Y.Event.define('flick', {

    on: function (node, subscriber, ce) {

        var startHandle = node.on(EVENT[START],
            this._onStart,
            this,
            node,
            subscriber,
            ce);

        subscriber[_FLICK_START_HANDLE] = startHandle;
    },

    detach: function (node, subscriber, ce) {

        var startHandle = subscriber[_FLICK_START_HANDLE],
            endHandle = subscriber[_FLICK_END_HANDLE];

        if (startHandle) {
            startHandle.detach();
            subscriber[_FLICK_START_HANDLE] = null;
        }

        if (endHandle) {
            endHandle.detach();
            subscriber[_FLICK_END_HANDLE] = null;
        }
    },

    processArgs: function(args) {
        var params = (args.length > 3) ? Y.merge(args.splice(3, 1)[0]) : {};

        if (!(MIN_VELOCITY in params)) {
            params[MIN_VELOCITY] = this.MIN_VELOCITY;
        }

        if (!(MIN_DISTANCE in params)) {
            params[MIN_DISTANCE] = this.MIN_DISTANCE;
        }

        if (!(PREVENT_DEFAULT in params)) {
            params[PREVENT_DEFAULT] = this.PREVENT_DEFAULT;
        }

        return params;
    },

    _onStart: function(e, node, subscriber, ce) {

        var start = true, // always true for mouse
            endHandle,
            moveHandle,
            doc,
            preventDefault = subscriber._extra.preventDefault,
            origE = e;

        if (e.touches) {
            start = (e.touches.length === 1);
            e = e.touches[0];
        }

        if (start) {

            if (preventDefault) {
                // preventDefault is a boolean or function
                if (!preventDefault.call || preventDefault(e)) {
                    origE.preventDefault();
                }
            }

            e.flick = {
                time : new Date().getTime()
            };

            subscriber[_FLICK_START] = e;

            endHandle = subscriber[_FLICK_END_HANDLE];

            doc = (node.get(NODE_TYPE) === 9) ? node : node.get(OWNER_DOCUMENT);
            if (!endHandle) {
                endHandle = doc.on(EVENT[END], Y.bind(this._onEnd, this), null, node, subscriber, ce);
                subscriber[_FLICK_END_HANDLE] = endHandle;
            }

            subscriber[_FLICK_MOVE_HANDLE] = doc.once(EVENT[MOVE], Y.bind(this._onMove, this), null, node, subscriber, ce);
        }
    },

    _onMove: function(e, node, subscriber, ce) {
        var start = subscriber[_FLICK_START];

        // Start timing from first move.
        if (start && start.flick) {
            start.flick.time = new Date().getTime();
        }
    },

    _onEnd: function(e, node, subscriber, ce) {

        var endTime = new Date().getTime(),
            start = subscriber[_FLICK_START],
            valid = !!start,
            endEvent = e,
            startTime,
            time,
            preventDefault,
            params,
            xyDistance,
            distance,
            velocity,
            axis,
            moveHandle = subscriber[_FLICK_MOVE_HANDLE];

        if (moveHandle) {
            moveHandle.detach();
            delete subscriber[_FLICK_MOVE_HANDLE];
        }

        if (valid) {

            if (e.changedTouches) {
                if (e.changedTouches.length === 1 && e.touches.length === 0) {
                    endEvent = e.changedTouches[0];
                } else {
                    valid = false;
                }
            }

            if (valid) {

                params = subscriber._extra;
                preventDefault = params[PREVENT_DEFAULT];

                if (preventDefault) {
                    // preventDefault is a boolean or function
                    if (!preventDefault.call || preventDefault(e)) {
                        e.preventDefault();
                    }
                }

                startTime = start.flick.time;
                endTime = new Date().getTime();
                time = endTime - startTime;

                xyDistance = [
                    endEvent.pageX - start.pageX,
                    endEvent.pageY - start.pageY
                ];

                if (params.axis) {
                    axis = params.axis;
                } else {
                    axis = (Math.abs(xyDistance[0]) >= Math.abs(xyDistance[1])) ? 'x' : 'y';
                }

                distance = xyDistance[(axis === 'x') ? 0 : 1];
                velocity = (time !== 0) ? distance/time : 0;

                if (isFinite(velocity) && (Math.abs(distance) >= params[MIN_DISTANCE]) && (Math.abs(velocity)  >= params[MIN_VELOCITY])) {

                    e.type = "flick";
                    e.flick = {
                        time:time,
                        distance: distance,
                        velocity:velocity,
                        axis: axis,
                        start : start
                    };

                    ce.fire(e);

                }

                subscriber[_FLICK_START] = null;
            }
        }
    },

    MIN_VELOCITY : 0,
    MIN_DISTANCE : 0,
    PREVENT_DEFAULT : false
});


}, '3.17.2', {"requires": ["node-base", "event-touch", "event-synthetic"]});
/*
YUI 3.17.2 (build 9c3c78e)
Copyright 2014 Yahoo! Inc. All rights reserved.
Licensed under the BSD License.
http://yuilibrary.com/license/
*/

YUI.add('event-valuechange', function (Y, NAME) {

/**
Adds a synthetic `valuechange` event that fires when the `value` property of an
`<input>`, `<textarea>`, `<select>`, or `[contenteditable="true"]` node changes
as a result of a keystroke, mouse operation, or input method editor (IME)
input event.

Usage:

    YUI().use('event-valuechange', function (Y) {
        Y.one('#my-input').on('valuechange', function (e) {
        });
    });

@module event-valuechange
**/

/**
Provides the implementation for the synthetic `valuechange` event. This class
isn't meant to be used directly, but is public to make monkeypatching possible.

Usage:

    YUI().use('event-valuechange', function (Y) {
        Y.one('#my-input').on('valuechange', function (e) {
        });
    });

@class ValueChange
@static
*/

var DATA_KEY = '_valuechange',
    VALUE    = 'value',
    NODE_NAME = 'nodeName',

    config, // defined at the end of this file

// Just a simple namespace to make methods overridable.
VC = {
    // -- Static Constants -----------------------------------------------------

    /**
    Interval (in milliseconds) at which to poll for changes to the value of an
    element with one or more `valuechange` subscribers when the user is likely
    to be interacting with it.

    @property POLL_INTERVAL
    @type Number
    @default 50
    @static
    **/
    POLL_INTERVAL: 50,

    /**
    Timeout (in milliseconds) after which to stop polling when there hasn't been
    any new activity (keypresses, mouse clicks, etc.) on an element.

    @property TIMEOUT
    @type Number
    @default 10000
    @static
    **/
    TIMEOUT: 10000,

    // -- Protected Static Methods ---------------------------------------------

    /**
    Called at an interval to poll for changes to the value of the specified
    node.

    @method _poll
    @param {Node} node Node to poll.

    @param {Object} options Options object.
        @param {EventFacade} [options.e] Event facade of the event that
            initiated the polling.

    @protected
    @static
    **/
    _poll: function (node, options) {
        var domNode  = node._node, // performance cheat; getValue() is a big hit when polling
            event    = options.e,
            vcData   = node._data && node._data[DATA_KEY], // another perf cheat
            stopped  = 0,
            facade, prevVal, newVal, nodeName, selectedOption, stopElement;

        if (!(domNode && vcData)) {
            VC._stopPolling(node);
            return;
        }

        prevVal = vcData.prevVal;
        nodeName  = vcData.nodeName;

        if (vcData.isEditable) {
            // Use innerHTML for performance
            newVal = domNode.innerHTML;
        } else if (nodeName === 'input' || nodeName === 'textarea') {
            // Use value property for performance
            newVal = domNode.value;
        } else if (nodeName === 'select') {
            // Back-compatibility with IE6 <select> element values.
            // Huge performance cheat to get past node.get('value').
            selectedOption = domNode.options[domNode.selectedIndex];
            newVal = selectedOption.value || selectedOption.text;
        }

        if (newVal !== prevVal) {
            vcData.prevVal = newVal;

            facade = {
                _event       : event,
                currentTarget: (event && event.currentTarget) || node,
                newVal       : newVal,
                prevVal      : prevVal,
                target       : (event && event.target) || node
            };

            Y.Object.some(vcData.notifiers, function (notifier) {
                var evt = notifier.handle.evt,
                    newStopped;

                // support e.stopPropagation()
                if (stopped !== 1) {
                    notifier.fire(facade);
                } else if (evt.el === stopElement) {
                    notifier.fire(facade);
                }

                newStopped = evt && evt._facade ? evt._facade.stopped : 0;

                // need to consider the condition in which there are two
                // listeners on the same element:
                // listener 1 calls e.stopPropagation()
                // listener 2 calls e.stopImmediatePropagation()
                if (newStopped > stopped) {
                    stopped = newStopped;

                    if (stopped === 1) {
                        stopElement = evt.el;
                    }
                }

                // support e.stopImmediatePropagation()
                if (stopped === 2) {
                    return true;
                }
            });

            VC._refreshTimeout(node);
        }
    },

    /**
    Restarts the inactivity timeout for the specified node.

    @method _refreshTimeout
    @param {Node} node Node to refresh.
    @param {SyntheticEvent.Notifier} notifier
    @protected
    @static
    **/
    _refreshTimeout: function (node, notifier) {
        // The node may have been destroyed, so check that it still exists
        // before trying to get its data. Otherwise an error will occur.
        if (!node._node) {
            return;
        }

        var vcData = node.getData(DATA_KEY);

        VC._stopTimeout(node); // avoid dupes

        // If we don't see any changes within the timeout period (10 seconds by
        // default), stop polling.
        vcData.timeout = setTimeout(function () {
            VC._stopPolling(node, notifier);
        }, VC.TIMEOUT);

    },

    /**
    Begins polling for changes to the `value` property of the specified node. If
    polling is already underway for the specified node, it will not be restarted
    unless the `force` option is `true`

    @method _startPolling
    @param {Node} node Node to watch.
    @param {SyntheticEvent.Notifier} notifier

    @param {Object} options Options object.
        @param {EventFacade} [options.e] Event facade of the event that
            initiated the polling.
        @param {Boolean} [options.force=false] If `true`, polling will be
            restarted even if we're already polling this node.

    @protected
    @static
    **/
    _startPolling: function (node, notifier, options) {
        var vcData, isEditable;

        if (!node.test('input,textarea,select') && !(isEditable = VC._isEditable(node))) {
            return;
        }

        vcData = node.getData(DATA_KEY);

        if (!vcData) {
            vcData = {
                nodeName   : node.get(NODE_NAME).toLowerCase(),
                isEditable : isEditable,
                prevVal    : isEditable ? node.getDOMNode().innerHTML : node.get(VALUE)
            };

            node.setData(DATA_KEY, vcData);
        }

        vcData.notifiers || (vcData.notifiers = {});

        // Don't bother continuing if we're already polling this node, unless
        // `options.force` is true.
        if (vcData.interval) {
            if (options.force) {
                VC._stopPolling(node, notifier); // restart polling, but avoid dupe polls
            } else {
                vcData.notifiers[Y.stamp(notifier)] = notifier;
                return;
            }
        }

        // Poll for changes to the node's value. We can't rely on keyboard
        // events for this, since the value may change due to a mouse-initiated
        // paste event, an IME input event, or for some other reason that
        // doesn't trigger a key event.
        vcData.notifiers[Y.stamp(notifier)] = notifier;

        vcData.interval = setInterval(function () {
            VC._poll(node, options);
        }, VC.POLL_INTERVAL);


        VC._refreshTimeout(node, notifier);
    },

    /**
    Stops polling for changes to the specified node's `value` attribute.

    @method _stopPolling
    @param {Node} node Node to stop polling on.
    @param {SyntheticEvent.Notifier} [notifier] Notifier to remove from the
        node. If not specified, all notifiers will be removed.
    @protected
    @static
    **/
    _stopPolling: function (node, notifier) {
        // The node may have been destroyed, so check that it still exists
        // before trying to get its data. Otherwise an error will occur.
        if (!node._node) {
            return;
        }

        var vcData = node.getData(DATA_KEY) || {};

        clearInterval(vcData.interval);
        delete vcData.interval;

        VC._stopTimeout(node);

        if (notifier) {
            vcData.notifiers && delete vcData.notifiers[Y.stamp(notifier)];
        } else {
            vcData.notifiers = {};
        }

    },

    /**
    Clears the inactivity timeout for the specified node, if any.

    @method _stopTimeout
    @param {Node} node
    @protected
    @static
    **/
    _stopTimeout: function (node) {
        var vcData = node.getData(DATA_KEY) || {};

        clearTimeout(vcData.timeout);
        delete vcData.timeout;
    },

    /**
    Check to see if a node has editable content or not.

    TODO: Add additional checks to get it to work for child nodes
    that inherit "contenteditable" from parent nodes. This may be
    too computationally intensive to be placed inside of the `_poll`
    loop, however.

    @method _isEditable
    @param {Node} node
    @protected
    @static
    **/
    _isEditable: function (node) {
        // Performance cheat because this is used inside `_poll`
        var domNode = node._node;
        return domNode.contentEditable === 'true' ||
               domNode.contentEditable === '';
    },



    // -- Protected Static Event Handlers --------------------------------------

    /**
    Stops polling when a node's blur event fires.

    @method _onBlur
    @param {EventFacade} e
    @param {SyntheticEvent.Notifier} notifier
    @protected
    @static
    **/
    _onBlur: function (e, notifier) {
        VC._stopPolling(e.currentTarget, notifier);
    },

    /**
    Resets a node's history and starts polling when a focus event occurs.

    @method _onFocus
    @param {EventFacade} e
    @param {SyntheticEvent.Notifier} notifier
    @protected
    @static
    **/
    _onFocus: function (e, notifier) {
        var node       = e.currentTarget,
            vcData     = node.getData(DATA_KEY);

        if (!vcData) {
            vcData = {
                isEditable : VC._isEditable(node),
                nodeName   : node.get(NODE_NAME).toLowerCase()
            };
            node.setData(DATA_KEY, vcData);
        }

        vcData.prevVal = vcData.isEditable ? node.getDOMNode().innerHTML : node.get(VALUE);

        VC._startPolling(node, notifier, {e: e});
    },

    /**
    Starts polling when a node receives a keyDown event.

    @method _onKeyDown
    @param {EventFacade} e
    @param {SyntheticEvent.Notifier} notifier
    @protected
    @static
    **/
    _onKeyDown: function (e, notifier) {
        VC._startPolling(e.currentTarget, notifier, {e: e});
    },

    /**
    Starts polling when an IME-related keyUp event occurs on a node.

    @method _onKeyUp
    @param {EventFacade} e
    @param {SyntheticEvent.Notifier} notifier
    @protected
    @static
    **/
    _onKeyUp: function (e, notifier) {
        // These charCodes indicate that an IME has started. We'll restart
        // polling and give the IME up to 10 seconds (by default) to finish.
        if (e.charCode === 229 || e.charCode === 197) {
            VC._startPolling(e.currentTarget, notifier, {
                e    : e,
                force: true
            });
        }
    },

    /**
    Starts polling when a node receives a mouseDown event.

    @method _onMouseDown
    @param {EventFacade} e
    @param {SyntheticEvent.Notifier} notifier
    @protected
    @static
    **/
    _onMouseDown: function (e, notifier) {
        VC._startPolling(e.currentTarget, notifier, {e: e});
    },

    /**
    Called when the `valuechange` event receives a new subscriber.

    Child nodes that aren't initially available when this subscription is
    called will still fire the `valuechange` event after their data is
    collected when the delegated `focus` event is captured. This includes
    elements that haven't been inserted into the DOM yet, as well as
    elements that aren't initially `contenteditable`.

    @method _onSubscribe
    @param {Node} node
    @param {Subscription} sub
    @param {SyntheticEvent.Notifier} notifier
    @param {Function|String} [filter] Filter function or selector string. Only
        provided for delegate subscriptions.
    @protected
    @static
    **/
    _onSubscribe: function (node, sub, notifier, filter) {
        var _valuechange, callbacks, isEditable, inputNodes, editableNodes;

        callbacks = {
            blur     : VC._onBlur,
            focus    : VC._onFocus,
            keydown  : VC._onKeyDown,
            keyup    : VC._onKeyUp,
            mousedown: VC._onMouseDown
        };

        // Store a utility object on the notifier to hold stuff that needs to be
        // passed around to trigger event handlers, polling handlers, etc.
        _valuechange = notifier._valuechange = {};

        if (filter) {
            // If a filter is provided, then this is a delegated subscription.
            _valuechange.delegated = true;

            // Add a function to the notifier that we can use to find all
            // nodes that pass the delegate filter.
            _valuechange.getNodes = function () {
                inputNodes    = node.all('input,textarea,select').filter(filter);
                editableNodes = node.all('[contenteditable="true"],[contenteditable=""]').filter(filter);

                return inputNodes.concat(editableNodes);
            };

            // Store the initial values for each descendant of the container
            // node that passes the delegate filter.
            _valuechange.getNodes().each(function (child) {
                if (!child.getData(DATA_KEY)) {
                    child.setData(DATA_KEY, {
                        nodeName   : child.get(NODE_NAME).toLowerCase(),
                        isEditable : VC._isEditable(child),
                        prevVal    : isEditable ? child.getDOMNode().innerHTML : child.get(VALUE)
                    });
                }
            });

            notifier._handles = Y.delegate(callbacks, node, filter, null,
                notifier);
        } else {
            isEditable = VC._isEditable(node);
            // This is a normal (non-delegated) event subscription.
            if (!node.test('input,textarea,select') && !isEditable) {
                return;
            }

            if (!node.getData(DATA_KEY)) {
                node.setData(DATA_KEY, {
                    nodeName   : node.get(NODE_NAME).toLowerCase(),
                    isEditable : isEditable,
                    prevVal    : isEditable ? node.getDOMNode().innerHTML : node.get(VALUE)
                });
            }

            notifier._handles = node.on(callbacks, null, null, notifier);
        }
    },

    /**
    Called when the `valuechange` event loses a subscriber.

    @method _onUnsubscribe
    @param {Node} node
    @param {Subscription} subscription
    @param {SyntheticEvent.Notifier} notifier
    @protected
    @static
    **/
    _onUnsubscribe: function (node, subscription, notifier) {
        var _valuechange = notifier._valuechange;

        notifier._handles && notifier._handles.detach();

        if (_valuechange.delegated) {
            _valuechange.getNodes().each(function (child) {
                VC._stopPolling(child, notifier);
            });
        } else {
            VC._stopPolling(node, notifier);
        }
    }
};

/**
Synthetic event that fires when the `value` property of an `<input>`,
`<textarea>`, `<select>`, or `[contenteditable="true"]` node changes as a
result of a user-initiated keystroke, mouse operation, or input method
editor (IME) input event.

Unlike the `onchange` event, this event fires when the value actually changes
and not when the element loses focus. This event also reports IME and
multi-stroke input more reliably than `oninput` or the various key events across
browsers.

For performance reasons, only focused nodes are monitored for changes, so
programmatic value changes on nodes that don't have focus won't be detected.

@example

    YUI().use('event-valuechange', function (Y) {
        Y.one('#my-input').on('valuechange', function (e) {
        });
    });

@event valuechange
@param {String} prevVal Previous value prior to the latest change.
@param {String} newVal New value after the latest change.
@for YUI
**/

config = {
    detach: VC._onUnsubscribe,
    on    : VC._onSubscribe,

    delegate      : VC._onSubscribe,
    detachDelegate: VC._onUnsubscribe,

    publishConfig: {
        emitFacade: true
    }
};

Y.Event.define('valuechange', config);
Y.Event.define('valueChange', config); // deprecated, but supported for backcompat

Y.ValueChange = VC;


}, '3.17.2', {"requires": ["event-focus", "event-synthetic"]});
/*
YUI 3.17.2 (build 9c3c78e)
Copyright 2014 Yahoo! Inc. All rights reserved.
Licensed under the BSD License.
http://yuilibrary.com/license/
*/

YUI.add('event-tap', function (Y, NAME) {

/**
The tap module provides a gesture events, "tap", which normalizes user interactions
across touch and mouse or pointer based input devices.  This can be used by application developers
to build input device agnostic components which behave the same in response to either touch or mouse based
interaction.

'tap' is like a touchscreen 'click', only it requires much less finger-down time since it listens to touch events,
but reverts to mouse events if touch is not supported.

@example

    YUI().use('event-tap', function (Y) {
        Y.one('#my-button').on('tap', function (e) {
        });
    });

@module event
@submodule event-tap
@author Andres Garza, matuzak and tilo mitra
@since 3.7.0

*/
var doc = Y.config.doc,
    GESTURE_MAP = Y.Event._GESTURE_MAP,
    EVT_START = GESTURE_MAP.start,
    EVT_TAP = 'tap',
    POINTER_EVENT_TEST = /pointer/i,

    HANDLES = {
        START: 'Y_TAP_ON_START_HANDLE',
        END: 'Y_TAP_ON_END_HANDLE',
        CANCEL: 'Y_TAP_ON_CANCEL_HANDLE'
    };

function detachHandles(subscription, handles) {
    handles = handles || Y.Object.values(HANDLES);

    Y.Array.each(handles, function (item) {
        var handle = subscription[item];
        if (handle) {
            handle.detach();
            subscription[item] = null;
        }
    });

}


/**
Sets up a "tap" event, that is fired on touch devices in response to a tap event (finger down, finder up).
This event can be used instead of listening for click events which have a 500ms delay on most touch devices.
This event can also be listened for using node.delegate().

@event tap
@param type {string} "tap"
@param fn {function} The method the event invokes. It receives the event facade of the underlying DOM event.
@for Event
@return {EventHandle} the detach handle
*/
Y.Event.define(EVT_TAP, {
    publishConfig: {
        preventedFn: function (e) {
            var sub = e.target.once('click', function (click) {
                click.preventDefault();
            });

            // Make sure to detach the subscription during the next event loop
            // so this doesn't `preventDefault()` on the wrong click event.
            setTimeout(function () {
                sub.detach();
            //Setting this to `0` causes the detachment to occur before the click
            //comes in on Android 4.0.3-4.0.4. 100ms seems to be a reliable number here
            //that works across the board.
            }, 100);
        }
    },

    processArgs: function (args, isDelegate) {

        //if we return for the delegate use case, then the `filter` argument
        //returns undefined, and we have to get the filter from sub._extra[0] (ugly)

        if (!isDelegate) {
            var extra = args[3];
            // remove the extra arguments from the array as specified by
            // http://yuilibrary.com/yui/docs/event/synths.html
            args.splice(3,1);
            return extra;
        }
    },
    /**
    This function should set up the node that will eventually fire the event.

    Usage:

        node.on('tap', function (e) {
        });

    @method on
    @param {Node} node
    @param {Array} subscription
    @param {Boolean} notifier
    @public
    @static
    **/
    on: function (node, subscription, notifier) {
        subscription[HANDLES.START] = node.on(EVT_START, this._start, this, node, subscription, notifier);
    },

    /**
    Detaches all event subscriptions set up by the event-tap module

    @method detach
    @param {Node} node
    @param {Array} subscription
    @param {Boolean} notifier
    @public
    @static
    **/
    detach: function (node, subscription, notifier) {
        detachHandles(subscription);
    },

    /**
    Event delegation for the 'tap' event. The delegated event will use a
    supplied selector or filtering function to test if the event references at least one
    node that should trigger the subscription callback.

    Usage:

        node.delegate('tap', function (e) {
        }, 'li a');

    @method delegate
    @param {Node} node
    @param {Array} subscription
    @param {Boolean} notifier
    @param {String | Function} filter
    @public
    @static
    **/
    delegate: function (node, subscription, notifier, filter) {
        subscription[HANDLES.START] = Y.delegate(EVT_START, function (e) {
            this._start(e, node, subscription, notifier, true);
        }, node, filter, this);
    },

    /**
    Detaches the delegated event subscriptions set up by the event-tap module.
    Only used if you use node.delegate(...) instead of node.on(...);

    @method detachDelegate
    @param {Node} node
    @param {Array} subscription
    @param {Boolean} notifier
    @public
    @static
    **/
    detachDelegate: function (node, subscription, notifier) {
        detachHandles(subscription);
    },

    /**
    Called when the monitor(s) are tapped on, either through touchstart or mousedown.

    @method _start
    @param {DOMEventFacade} event
    @param {Node} node
    @param {Array} subscription
    @param {Boolean} notifier
    @param {Boolean} delegate
    @protected
    @static
    **/
    _start: function (event, node, subscription, notifier, delegate) {

        var context = {
                canceled: false,
                eventType: event.type
            },
            preventMouse = subscription.preventMouse || false;

        //move ways to quit early to the top.
        // no right clicks
        if (event.button && event.button === 3) {
            return;
        }

        // for now just support a 1 finger count (later enhance via config)
        if (event.touches && event.touches.length !== 1) {
            return;
        }

        context.node = delegate ? event.currentTarget : node;

        //There is a double check in here to support event simulation tests, in which
        //event.touches can be undefined when simulating 'touchstart' on touch devices.
        if (event.touches) {
          context.startXY = [ event.touches[0].pageX, event.touches[0].pageY ];
        }
        else {
          context.startXY = [ event.pageX, event.pageY ];
        }

        //If `onTouchStart()` was called by a touch event, set up touch event subscriptions.
        //Otherwise, set up mouse/pointer event event subscriptions.
        if (event.touches) {

            subscription[HANDLES.END] = node.once('touchend', this._end, this, node, subscription, notifier, delegate, context);
            subscription[HANDLES.CANCEL] = node.once('touchcancel', this.detach, this, node, subscription, notifier, delegate, context);

            //Since this is a touch* event, there will be corresponding mouse events
            //that will be fired. We don't want these events to get picked up and fire
            //another `tap` event, so we'll set this variable to `true`.
            subscription.preventMouse = true;
        }

        //Only add these listeners if preventMouse is `false`
        //ie: not when touch events have already been subscribed to
        else if (context.eventType.indexOf('mouse') !== -1 && !preventMouse) {
            subscription[HANDLES.END] = node.once('mouseup', this._end, this, node, subscription, notifier, delegate, context);
            subscription[HANDLES.CANCEL] = node.once('mousecancel', this.detach, this, node, subscription, notifier, delegate, context);
        }

        //If a mouse event comes in after a touch event, it will go in here and
        //reset preventMouse to `true`.
        //If a mouse event comes in without a prior touch event, preventMouse will be
        //false in any case, so this block doesn't do anything.
        else if (context.eventType.indexOf('mouse') !== -1 && preventMouse) {
            subscription.preventMouse = false;
        }

        else if (POINTER_EVENT_TEST.test(context.eventType)) {
            subscription[HANDLES.END] = node.once(GESTURE_MAP.end, this._end, this, node, subscription, notifier, delegate, context);
            subscription[HANDLES.CANCEL] = node.once(GESTURE_MAP.cancel, this.detach, this, node, subscription, notifier, delegate, context);
        }

    },


    /**
    Called when the monitor(s) fires a touchend event (or the mouse equivalent).
    This method fires the 'tap' event if certain requirements are met.

    @method _end
    @param {DOMEventFacade} event
    @param {Node} node
    @param {Array} subscription
    @param {Boolean} notifier
    @param {Boolean} delegate
    @param {Object} context
    @protected
    @static
    **/
    _end: function (event, node, subscription, notifier, delegate, context) {
        var startXY = context.startXY,
            endXY,
            clientXY,
            sensitivity = 15;

        if (subscription._extra && subscription._extra.sensitivity >= 0) {
            sensitivity = subscription._extra.sensitivity;
        }

        //There is a double check in here to support event simulation tests, in which
        //event.touches can be undefined when simulating 'touchstart' on touch devices.
        if (event.changedTouches) {
          endXY = [ event.changedTouches[0].pageX, event.changedTouches[0].pageY ];
          clientXY = [event.changedTouches[0].clientX, event.changedTouches[0].clientY];
        }
        else {
          endXY = [ event.pageX, event.pageY ];
          clientXY = [event.clientX, event.clientY];
        }

        // make sure mouse didn't move
        if (Math.abs(endXY[0] - startXY[0]) <= sensitivity && Math.abs(endXY[1] - startXY[1]) <= sensitivity) {

            event.type = EVT_TAP;
            event.pageX = endXY[0];
            event.pageY = endXY[1];
            event.clientX = clientXY[0];
            event.clientY = clientXY[1];
            event.currentTarget = context.node;

            notifier.fire(event);
        }

        detachHandles(subscription, [HANDLES.END, HANDLES.CANCEL]);
    }
});


}, '3.17.2', {"requires": ["node-base", "event-base", "event-touch", "event-synthetic"]});
