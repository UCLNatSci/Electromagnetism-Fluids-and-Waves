(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
'use strict';var m;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ba="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function ca(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var da=ca(this);function t(a,b){if(b)a:{var c=da;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&ba(c,a,{configurable:!0,writable:!0,value:b})}}
t("Symbol",function(a){function b(f){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c(d+(f||"")+"_"+e++,f)}
function c(f,g){this.h=f;ba(this,"description",{configurable:!0,writable:!0,value:g})}
if(a)return a;c.prototype.toString=function(){return this.h};
var d="jscomp_symbol_"+(1E9*Math.random()>>>0)+"_",e=0;return b});
t("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=da[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ba(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ea(aa(this))}})}return a});
function ea(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function u(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}}
function fa(a){if(!(a instanceof Array)){a=u(a);for(var b,c=[];!(b=a.next()).done;)c.push(b.value);a=c}return a}
var ha="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ia=function(){function a(){function c(){}
new c;Reflect.construct(c,[],function(){});
return new c instanceof c}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(c,d,e){c=b(c,d);e&&Reflect.setPrototypeOf(c,e.prototype);return c}}return function(c,d,e){void 0===e&&(e=c);
e=ha(e.prototype||Object.prototype);return Function.prototype.apply.call(c,e,d)||e}}(),ja;
if("function"==typeof Object.setPrototypeOf)ja=Object.setPrototypeOf;else{var ka;a:{var la={a:!0},ma={};try{ma.__proto__=la;ka=ma.a;break a}catch(a){}ka=!1}ja=ka?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var na=ja;
function v(a,b){a.prototype=ha(b.prototype);a.prototype.constructor=a;if(na)na(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.L=b.prototype}
function oa(){this.o=!1;this.l=null;this.i=void 0;this.h=1;this.u=this.m=0;this.C=this.j=null}
function pa(a){if(a.o)throw new TypeError("Generator is already running");a.o=!0}
oa.prototype.A=function(a){this.i=a};
function qa(a,b){a.j={Ha:b,Ia:!0};a.h=a.m||a.u}
oa.prototype.return=function(a){this.j={return:a};this.h=this.u};
function w(a,b,c){a.h=c;return{value:b}}
oa.prototype.B=function(a){this.h=a};
function ra(a,b,c){a.m=b;void 0!=c&&(a.u=c)}
function sa(a){a.m=0;var b=a.j.Ha;a.j=null;return b}
function ta(a){a.C=[a.j];a.m=0;a.u=0}
function ua(a){var b=a.C.splice(0)[0];(b=a.j=a.j||b)?b.Ia?a.h=a.m||a.u:void 0!=b.B&&a.u<b.B?(a.h=b.B,a.j=null):a.h=a.u:a.h=0}
function va(a){this.h=new oa;this.i=a}
function wa(a,b){pa(a.h);var c=a.h.l;if(c)return xa(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.h.return);
a.h.return(b);return ya(a)}
function xa(a,b,c,d){try{var e=b.call(a.h.l,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.h.o=!1,e;var f=e.value}catch(g){return a.h.l=null,qa(a.h,g),ya(a)}a.h.l=null;d.call(a.h,f);return ya(a)}
function ya(a){for(;a.h.h;)try{var b=a.i(a.h);if(b)return a.h.o=!1,{value:b.value,done:!1}}catch(c){a.h.i=void 0,qa(a.h,c)}a.h.o=!1;if(a.h.j){b=a.h.j;a.h.j=null;if(b.Ia)throw b.Ha;return{value:b.return,done:!0}}return{value:void 0,done:!0}}
function za(a){this.next=function(b){pa(a.h);a.h.l?b=xa(a,a.h.l.next,b,a.h.A):(a.h.A(b),b=ya(a));return b};
this.throw=function(b){pa(a.h);a.h.l?b=xa(a,a.h.l["throw"],b,a.h.A):(qa(a.h,b),b=ya(a));return b};
this.return=function(b){return wa(a,b)};
this[Symbol.iterator]=function(){return this}}
function x(a,b){b=new za(new va(b));na&&a.prototype&&na(b,a.prototype);return b}
t("Reflect",function(a){return a?a:{}});
t("Reflect.construct",function(){return ia});
t("Reflect.setPrototypeOf",function(a){return a?a:na?function(b,c){try{return na(b,c),!0}catch(d){return!1}}:null});
function Aa(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
t("WeakMap",function(a){function b(k){this.h=(h+=Math.random()+1).toString();if(k){k=u(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!Aa(k,g)){var l=new c;ba(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(n){if(n instanceof c)return n;Object.isExtensible(n)&&e(n);return l(n)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),n=new a([[k,2],[l,3]]);if(2!=n.get(k)||3!=n.get(l))return!1;n.delete(k);n.set(l,4);return!n.has(k)&&4==n.get(l)}catch(q){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!Aa(k,g))throw Error("WeakMap key fail: "+k);k[g][this.h]=l;return this};
b.prototype.get=function(k){return d(k)&&Aa(k,g)?k[g][this.h]:void 0};
b.prototype.has=function(k){return d(k)&&Aa(k,g)&&Aa(k[g],this.h)};
b.prototype.delete=function(k){return d(k)&&Aa(k,g)&&Aa(k[g],this.h)?delete k[g][this.h]:!1};
return b});
t("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h.h;return ea(function(){if(l){for(;l.head!=h.h;)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var n=h.data_[l];if(n&&Aa(h.data_,l))for(h=0;h<n.length;h++){var q=n[h];if(k!==k&&q.key!==q.key||k===q.key)return{id:l,list:n,index:h,G:q}}return{id:l,list:n,index:-1,G:void 0}}
function e(h){this.data_={};this.h=b();this.size=0;if(h){h=u(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(u([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),n=l.next();if(n.done||n.value[0]!=h||"s"!=n.value[1])return!1;n=l.next();return n.done||4!=n.value[0].x||"t"!=n.value[1]||!l.next().done?!1:!0}catch(q){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this.data_[l.id]=[]);l.G?l.G.value=k:(l.G={next:this.h,previous:this.h.previous,head:this.h,key:h,value:k},l.list.push(l.G),this.h.previous.next=l.G,this.h.previous=l.G,this.size++);return this};
e.prototype.delete=function(h){h=d(this,h);return h.G&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.data_[h.id],h.G.previous.next=h.G.next,h.G.next.previous=h.G.previous,h.G.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.data_={};this.h=this.h.previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).G};
e.prototype.get=function(h){return(h=d(this,h).G)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),n;!(n=l.next()).done;)n=n.value,h.call(k,n[1],n[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
function Ba(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
t("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=Ba(this,b,"endsWith");b+="";void 0===c&&(c=d.length);c=Math.max(0,Math.min(c|0,d.length));for(var e=b.length;0<e&&0<c;)if(d[--c]!=b[--e])return!1;return 0>=e}});
t("Array.prototype.find",function(a){return a?a:function(b,c){a:{var d=this;d instanceof String&&(d=String(d));for(var e=d.length,f=0;f<e;f++){var g=d[f];if(b.call(c,g,f,d)){b=g;break a}}b=void 0}return b}});
t("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=Ba(this,b,"startsWith");b+="";var e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});
t("Object.setPrototypeOf",function(a){return a||na});
var Ca="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)Aa(d,e)&&(a[e]=d[e])}return a};
t("Object.assign",function(a){return a||Ca});
t("Promise",function(a){function b(g){this.h=0;this.j=void 0;this.i=[];this.o=!1;var h=this.l();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.h=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.i=function(g){if(null==this.h){this.h=[];var h=this;this.j(function(){h.u()})}this.h.push(g)};
var e=da.setTimeout;c.prototype.j=function(g){e(g,0)};
c.prototype.u=function(){for(;this.h&&this.h.length;){var g=this.h;this.h=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.l(l)}}}this.h=null};
c.prototype.l=function(g){this.j(function(){throw g;})};
b.prototype.l=function(){function g(l){return function(n){k||(k=!0,l.call(h,n))}}
var h=this,k=!1;return{resolve:g(this.M),reject:g(this.u)}};
b.prototype.M=function(g){if(g===this)this.u(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.Z(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.I(g):this.m(g)}};
b.prototype.I=function(g){var h=void 0;try{h=g.then}catch(k){this.u(k);return}"function"==typeof h?this.aa(h,g):this.m(g)};
b.prototype.u=function(g){this.A(2,g)};
b.prototype.m=function(g){this.A(1,g)};
b.prototype.A=function(g,h){if(0!=this.h)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.h);this.h=g;this.j=h;2===this.h&&this.N();this.C()};
b.prototype.N=function(){var g=this;e(function(){if(g.F()){var h=da.console;"undefined"!==typeof h&&h.error(g.j)}},1)};
b.prototype.F=function(){if(this.o)return!1;var g=da.CustomEvent,h=da.Event,k=da.dispatchEvent;if("undefined"===typeof k)return!0;"function"===typeof g?g=new g("unhandledrejection",{cancelable:!0}):"function"===typeof h?g=new h("unhandledrejection",{cancelable:!0}):(g=da.document.createEvent("CustomEvent"),g.initCustomEvent("unhandledrejection",!1,!0,g));g.promise=this;g.reason=this.j;return k(g)};
b.prototype.C=function(){if(null!=this.i){for(var g=0;g<this.i.length;++g)f.i(this.i[g]);this.i=null}};
var f=new c;b.prototype.Z=function(g){var h=this.l();g.ha(h.resolve,h.reject)};
b.prototype.aa=function(g,h){var k=this.l();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(r,p){return"function"==typeof r?function(z){try{l(r(z))}catch(I){n(I)}}:p}
var l,n,q=new b(function(r,p){l=r;n=p});
this.ha(k(g,l),k(h,n));return q};
b.prototype.catch=function(g){return this.then(void 0,g)};
b.prototype.ha=function(g,h){function k(){switch(l.h){case 1:g(l.j);break;case 2:h(l.j);break;default:throw Error("Unexpected state: "+l.h);}}
var l=this;null==this.i?f.i(k):this.i.push(k);this.o=!0};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=u(g),n=l.next();!n.done;n=l.next())d(n.value).ha(h,k)})};
b.all=function(g){var h=u(g),k=h.next();return k.done?d([]):new b(function(l,n){function q(z){return function(I){r[z]=I;p--;0==p&&l(r)}}
var r=[],p=0;do r.push(void 0),p++,d(k.value).ha(q(r.length-1),n),k=h.next();while(!k.done)})};
return b});
function Da(a,b){a instanceof String&&(a+="");var c=0,d=!1,e={next:function(){if(!d&&c<a.length){var f=c++;return{value:b(f,a[f]),done:!1}}d=!0;return{done:!0,value:void 0}}};
e[Symbol.iterator]=function(){return e};
return e}
t("Array.prototype.entries",function(a){return a?a:function(){return Da(this,function(b,c){return[b,c]})}});
t("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)Aa(b,d)&&c.push([d,b[d]]);return c}});
t("Array.prototype.keys",function(a){return a?a:function(){return Da(this,function(b){return b})}});
t("Array.prototype.values",function(a){return a?a:function(){return Da(this,function(b,c){return c})}});
t("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
t("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});
t("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==Ba(this,b,"includes").indexOf(b,c||0)}});
t("Set",function(a){function b(c){this.h=new Map;if(c){c=u(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.h.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(u([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.h.set(c,c);this.size=this.h.size;return this};
b.prototype.delete=function(c){c=this.h.delete(c);this.size=this.h.size;return c};
b.prototype.clear=function(){this.h.clear();this.size=0};
b.prototype.has=function(c){return this.h.has(c)};
b.prototype.entries=function(){return this.h.entries()};
b.prototype.values=function(){return this.h.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.h.forEach(function(f){return c.call(d,f,f,e)})};
return b});
t("Array.from",function(a){return a?a:function(b,c,d){c=null!=c?c:function(h){return h};
var e=[],f="undefined"!=typeof Symbol&&Symbol.iterator&&b[Symbol.iterator];if("function"==typeof f){b=f.call(b);for(var g=0;!(f=b.next()).done;)e.push(c.call(d,f.value,g++))}else for(f=b.length,g=0;g<f;g++)e.push(c.call(d,b[g],g));return e}});
t("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});
t("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});
t("Object.values",function(a){return a?a:function(b){var c=[],d;for(d in b)Aa(b,d)&&c.push(b[d]);return c}});
var y=this||self;function A(a,b,c){a=a.split(".");c=c||y;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function B(a,b){a=a.split(".");b=b||y;for(var c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function Ea(){}
function Fa(a){a.xa=void 0;a.getInstance=function(){return a.xa?a.xa:a.xa=new a}}
function Ga(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Ha(a){var b=Ga(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Ia(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Ka(a){return Object.prototype.hasOwnProperty.call(a,La)&&a[La]||(a[La]=++Ma)}
var La="closure_uid_"+(1E9*Math.random()>>>0),Ma=0;function Na(a,b,c){return a.call.apply(a.bind,arguments)}
function Oa(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function Pa(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?Pa=Na:Pa=Oa;return Pa.apply(null,arguments)}
function Qa(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
function Ra(a,b){A(a,b,void 0)}
function C(a,b){function c(){}
c.prototype=b.prototype;a.L=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Ml=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}}
function Sa(a){return a}
;function Ta(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,Ta);else{var c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));void 0!==b&&(this.Qa=b)}
C(Ta,Error);Ta.prototype.name="CustomError";function Ua(a){a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.j=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.h=/[?&]adurl=([^&]*)/.exec(a))&&this.h[1]){try{var c=decodeURIComponent(this.h[1])}catch(d){c=null}this.i=c}}
;function Va(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;var Wa=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},D=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Xa=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f="string"===typeof a?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},Ya=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},Za=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
D(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function $a(a,b){a:{for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return 0>b?null:"string"===typeof a?a.charAt(b):a[b]}
function ab(a,b){b=Wa(a,b);var c;(c=0<=b)&&Array.prototype.splice.call(a,b,1);return c}
function bb(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function cb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Ha(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function db(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function eb(a){var b=fb,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function gb(a){for(var b in a)return!1;return!0}
function hb(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function ib(){var a=F("PLAYER_VARS",{});return null!==a&&"privembed"in a?a.privembed:!1}
function jb(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function kb(a){var b={},c;for(c in a)b[c]=a[c];return b}
function lb(a){if(!a||"object"!==typeof a)return a;if("function"===typeof a.clone)return a.clone();if("undefined"!==typeof Map&&a instanceof Map)return new Map(a);if("undefined"!==typeof Set&&a instanceof Set)return new Set(a);var b=Array.isArray(a)?[]:"function"!==typeof ArrayBuffer||"function"!==typeof ArrayBuffer.isView||!ArrayBuffer.isView(a)||a instanceof DataView?{}:new a.constructor(a.length),c;for(c in a)b[c]=lb(a[c]);return b}
var mb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function nb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<mb.length;f++)c=mb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var ob;function pb(){if(void 0===ob){var a=null,b=y.trustedTypes;if(b&&b.createPolicy){try{a=b.createPolicy("goog#html",{createHTML:Sa,createScript:Sa,createScriptURL:Sa})}catch(c){y.console&&y.console.error(c.message)}ob=a}else ob=a}return ob}
;function qb(a,b){this.h=a===rb&&b||""}
qb.prototype.R=!0;qb.prototype.P=function(){return this.h};
function sb(a){return new qb(rb,a)}
var rb={};sb("");var tb={};function ub(a){this.h=tb===tb?a:"";this.R=!0}
ub.prototype.P=function(){return this.h.toString()};
ub.prototype.toString=function(){return this.h.toString()};function vb(a,b){this.h=b===wb?a:""}
m=vb.prototype;m.R=!0;m.P=function(){return this.h.toString()};
m.wa=!0;m.ra=function(){return 1};
m.toString=function(){return this.h+""};
function xb(a){if(a instanceof vb&&a.constructor===vb)return a.h;Ga(a);return"type_error:TrustedResourceUrl"}
var wb={};function yb(a){var b=pb();a=b?b.createScriptURL(a):a;return new vb(a,wb)}
;var zb=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]},Ab=/&/g,Bb=/</g,Cb=/>/g,Db=/"/g,Eb=/'/g,Fb=/\x00/g,Gb=/[\x00&<>"']/;function Hb(a,b){this.h=b===Ib?a:""}
m=Hb.prototype;m.R=!0;m.P=function(){return this.h.toString()};
m.wa=!0;m.ra=function(){return 1};
m.toString=function(){return this.h.toString()};
function Jb(a){if(a instanceof Hb&&a.constructor===Hb)return a.h;Ga(a);return"type_error:SafeUrl"}
var Kb=RegExp('^(?:audio/(?:3gpp2|3gpp|aac|L16|midi|mp3|mp4|mpeg|oga|ogg|opus|x-m4a|x-matroska|x-wav|wav|webm)|font/\\w+|image/(?:bmp|gif|jpeg|jpg|png|tiff|webp|x-icon)|video/(?:mpeg|mp4|ogg|webm|quicktime|x-matroska))(?:;\\w+=(?:\\w+|"[\\w;,= ]+"))*$',"i"),Lb=/^data:(.*);base64,[a-z0-9+\/]+=*$/i,Mb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i,Ib={},Nb=new Hb("about:invalid#zClosurez",Ib);var Ob;a:{var Pb=y.navigator;if(Pb){var Qb=Pb.userAgent;if(Qb){Ob=Qb;break a}}Ob=""}function G(a){return-1!=Ob.indexOf(a)}
;function Rb(){return G("Firefox")||G("FxiOS")}
function Sb(){return(G("Chrome")||G("CriOS"))&&!G("Edge")}
;var Tb={};function Ub(a,b,c){this.h=c===Tb?a:"";this.i=b;this.R=this.wa=!0}
Ub.prototype.ra=function(){return this.i};
Ub.prototype.P=function(){return this.h.toString()};
Ub.prototype.toString=function(){return this.h.toString()};
function Vb(a,b){var c=pb();a=c?c.createHTML(a):a;return new Ub(a,b,Tb)}
;function Wb(a,b){b instanceof Hb||b instanceof Hb||(b="object"==typeof b&&b.R?b.P():String(b),Mb.test(b)||(b="about:invalid#zClosurez"),b=new Hb(b,Ib));a.href=Jb(b)}
function Xb(a,b){a.rel="stylesheet";a.href=xb(b).toString();(b=Yb('style[nonce],link[rel="stylesheet"][nonce]',a.ownerDocument&&a.ownerDocument.defaultView))&&a.setAttribute("nonce",b)}
function Zb(){return Yb("script[nonce]",void 0)}
var $b=/^[\w+/_-]+[=]{0,2}$/;function Yb(a,b){b=(b||y).document;return b.querySelector?(a=b.querySelector(a))&&(a=a.nonce||a.getAttribute("nonce"))&&$b.test(a)?a:"":""}
;function ac(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var bc=RegExp("^(?:([^:/?#.]+):)?(?://(?:([^\\\\/?#]*)@)?([^\\\\/?#]*?)(?::([0-9]+))?(?=[\\\\/?#]|$))?([^?#]+)?(?:\\?([^#]*))?(?:#([\\s\\S]*))?$");function cc(a){return a?decodeURI(a):a}
function dc(a){return cc(a.match(bc)[3]||null)}
function ec(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)ec(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function fc(a){var b=[],c;for(c in a)ec(c,a[c],b);return b.join("&")}
function gc(a,b){b=fc(b);if(b){var c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);a=[a.substr(0,d),e,a.substr(c)];c=a[1];a[1]=b?c?c+"&"+b:b:c;b=a[0]+(a[1]?"?"+a[1]:"")+a[2]}else b=a;return b}
var hc=/#|$/;function H(a,b){var c=void 0;return new (c||(c=Promise))(function(d,e){function f(k){try{h(b.next(k))}catch(l){e(l)}}
function g(k){try{h(b["throw"](k))}catch(l){e(l)}}
function h(k){k.done?d(k.value):(new c(function(l){l(k.value)})).then(f,g)}
h((b=b.apply(a,void 0)).next())})}
;function ic(){return G("iPhone")&&!G("iPod")&&!G("iPad")}
;function jc(a){jc[" "](a);return a}
jc[" "]=Ea;var kc=G("Opera"),lc=G("Trident")||G("MSIE"),mc=G("Edge"),nc=G("Gecko")&&!(-1!=Ob.toLowerCase().indexOf("webkit")&&!G("Edge"))&&!(G("Trident")||G("MSIE"))&&!G("Edge"),oc=-1!=Ob.toLowerCase().indexOf("webkit")&&!G("Edge"),pc=G("Android");function qc(){var a=y.document;return a?a.documentMode:void 0}
var rc;a:{var sc="",tc=function(){var a=Ob;if(nc)return/rv:([^\);]+)(\)|;)/.exec(a);if(mc)return/Edge\/([\d\.]+)/.exec(a);if(lc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(oc)return/WebKit\/(\S+)/.exec(a);if(kc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
tc&&(sc=tc?tc[1]:"");if(lc){var uc=qc();if(null!=uc&&uc>parseFloat(sc)){rc=String(uc);break a}}rc=sc}var vc=rc,wc;if(y.document&&lc){var xc=qc();wc=xc?xc:parseInt(vc,10)||void 0}else wc=void 0;var yc=wc;Rb();var zc=ic()||G("iPod"),Ac=G("iPad");!G("Android")||Sb()||Rb();Sb();var Bc=G("Safari")&&!(Sb()||G("Coast")||G("Opera")||G("Edge")||G("Edg/")||G("OPR")||Rb()||G("Silk")||G("Android"))&&!(ic()||G("iPad")||G("iPod"));var Cc={},Dc=null;
function Ec(a){var b=3;Ha(a);void 0===b&&(b=0);if(!Dc){Dc={};for(var c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),d=["+/=","+/","-_=","-_.","-_"],e=0;5>e;e++){var f=c.concat(d[e].split(""));Cc[e]=f;for(var g=0;g<f.length;g++){var h=f[g];void 0===Dc[h]&&(Dc[h]=g)}}}b=Cc[b];c=Array(Math.floor(a.length/3));d=b[64]||"";for(e=f=0;f<a.length-2;f+=3){var k=a[f],l=a[f+1];h=a[f+2];g=b[k>>2];k=b[(k&3)<<4|l>>4];l=b[(l&15)<<2|h>>6];h=b[h&63];c[e++]=""+g+k+l+h}g=0;h=d;switch(a.length-
f){case 2:g=a[f+1],h=b[(g&15)<<2]||d;case 1:a=a[f],c[e]=""+b[a>>2]+b[(a&3)<<4|g>>4]+h+d}return c.join("")}
;var Fc={Ol:{value:!0,configurable:!0}};var Gc=Object,Hc=Gc.freeze,Ic=[];Array.isArray(Ic)&&!Object.isFrozen(Ic)&&Object.defineProperties(Ic,Fc);Hc.call(Gc,Ic);var K=window;sb("csi.gstatic.com");sb("googleads.g.doubleclick.net");sb("pagead2.googlesyndication.com");sb("partner.googleadservices.com");sb("pubads.g.doubleclick.net");sb("securepubads.g.doubleclick.net");sb("tpc.googlesyndication.com");var Jc={};function Kc(){}
function Lc(a){this.h=a}
v(Lc,Kc);Lc.prototype.toString=function(){return this.h};
var Mc=new Lc("about:invalid#zTSz",Jc);function Nc(a){if(a instanceof Kc)if(a instanceof Lc)a=a.h;else throw Error("");else a=Jb(a);return a}
;function Oc(a,b){a.src=xb(b);var c;b=(a.ownerDocument&&a.ownerDocument.defaultView||window).document;var d=null===(c=b.querySelector)||void 0===c?void 0:c.call(b,"script[nonce]");(c=d?d.nonce||d.getAttribute("nonce")||"":"")&&a.setAttribute("nonce",c)}
;function Pc(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
m=Pc.prototype;m.clone=function(){return new Pc(this.x,this.y)};
m.equals=function(a){return a instanceof Pc&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
m.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
m.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
m.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Qc(a,b){this.width=a;this.height=b}
m=Qc.prototype;m.clone=function(){return new Qc(this.width,this.height)};
m.aspectRatio=function(){return this.width/this.height};
m.isEmpty=function(){return!(this.width*this.height)};
m.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
m.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
m.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Rc(a){var b=document;return"string"===typeof a?b.getElementById(a):a}
function Sc(a,b){db(b,function(c,d){c&&"object"==typeof c&&c.R&&(c=c.P());"style"==d?a.style.cssText=c:"class"==d?a.className=c:"for"==d?a.htmlFor=c:Tc.hasOwnProperty(d)?a.setAttribute(Tc[d],c):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,c):a[d]=c})}
var Tc={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};function Uc(a,b,c){var d=arguments,e=document,f=d[1],g=Vc(e,String(d[0]));f&&("string"===typeof f?g.className=f:Array.isArray(f)?g.className=f.join(" "):Sc(g,f));2<d.length&&Wc(e,g,d);return g}
function Wc(a,b,c){function d(h){h&&b.appendChild("string"===typeof h?a.createTextNode(h):h)}
for(var e=2;e<c.length;e++){var f=c[e];if(!Ha(f)||Ia(f)&&0<f.nodeType)d(f);else{a:{if(f&&"number"==typeof f.length){if(Ia(f)){var g="function"==typeof f.item||"string"==typeof f.item;break a}if("function"===typeof f){g="function"==typeof f.item;break a}}g=!1}D(g?bb(f):f,d)}}}
function Vc(a,b){b=String(b);"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)}
function Xc(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Yc(a){var b=Zc;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a.call(void 0,b[c],c,b)}
function $c(){var a=[];Yc(function(b){a.push(b)});
return a}
var Zc={Ib:"allow-forms",Jb:"allow-modals",Kb:"allow-orientation-lock",Lb:"allow-pointer-lock",Mb:"allow-popups",Nb:"allow-popups-to-escape-sandbox",Ob:"allow-presentation",Pb:"allow-same-origin",Qb:"allow-scripts",Rb:"allow-top-navigation",Sb:"allow-top-navigation-by-user-activation"},ad=Va(function(){return $c()});
function bd(){var a=Vc(document,"IFRAME"),b={};D(ad(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
;function cd(a){this.isValid=a}
function dd(a){return new cd(function(b){return b.substr(0,a.length+1).toLowerCase()===a+":"})}
var ed=[dd("data"),dd("http"),dd("https"),dd("mailto"),dd("ftp"),new cd(function(a){return/^[^:]*([/?#]|$)/.test(a)})];function fd(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var gd=(new Date).getTime();function hd(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));c=a.substring(0,a.indexOf("://"));if(!c)throw Error("URI is missing protocol: "+a);if("http"!==c&&"https"!==c&&"chrome-extension"!==c&&"moz-extension"!==c&&"file"!==c&&"android-app"!==c&&"chrome-search"!==c&&"chrome-untrusted"!==c&&"chrome"!==
c&&"app"!==c&&"devtools"!==c)throw Error("Invalid URI scheme in origin: "+c);a="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===c&&"80"!==e||"https"===c&&"443"!==e)a=":"+e}return c+"://"+b+a}
;function id(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;n=l=0}
function b(q){for(var r=g,p=0;64>p;p+=4)r[p/4]=q[p]<<24|q[p+1]<<16|q[p+2]<<8|q[p+3];for(p=16;80>p;p++)q=r[p-3]^r[p-8]^r[p-14]^r[p-16],r[p]=(q<<1|q>>>31)&4294967295;q=e[0];var z=e[1],I=e[2],E=e[3],R=e[4];for(p=0;80>p;p++){if(40>p)if(20>p){var V=E^z&(I^E);var J=1518500249}else V=z^I^E,J=1859775393;else 60>p?(V=z&I|E&(z|I),J=2400959708):(V=z^I^E,J=3395469782);V=((q<<5|q>>>27)&4294967295)+V+R+J+r[p]&4294967295;R=E;E=I;I=(z<<30|z>>>2)&4294967295;z=q;q=V}e[0]=e[0]+q&4294967295;e[1]=e[1]+z&4294967295;e[2]=
e[2]+I&4294967295;e[3]=e[3]+E&4294967295;e[4]=e[4]+R&4294967295}
function c(q,r){if("string"===typeof q){q=unescape(encodeURIComponent(q));for(var p=[],z=0,I=q.length;z<I;++z)p.push(q.charCodeAt(z));q=p}r||(r=q.length);p=0;if(0==l)for(;p+64<r;)b(q.slice(p,p+64)),p+=64,n+=64;for(;p<r;)if(f[l++]=q[p++],n++,64==l)for(l=0,b(f);p+64<r;)b(q.slice(p,p+64)),p+=64,n+=64}
function d(){var q=[],r=8*n;56>l?c(h,56-l):c(h,64-(l-56));for(var p=63;56<=p;p--)f[p]=r&255,r>>>=8;b(f);for(p=r=0;5>p;p++)for(var z=24;0<=z;z-=8)q[r++]=e[p]>>z&255;return q}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,n;a();return{reset:a,update:c,digest:d,Ra:function(){for(var q=d(),r="",p=0;p<q.length;p++)r+="0123456789ABCDEF".charAt(Math.floor(q[p]/16))+"0123456789ABCDEF".charAt(q[p]%16);return r}}}
;function jd(a,b,c){var d=String(y.location.href);return d&&a&&b?[b,kd(hd(d),a,c||null)].join(" "):null}
function kd(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],D(d,function(h){e.push(h)}),ld(e.join(" "));
var f=[],g=[];D(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];D(d,function(h){e.push(h)});
a=ld(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function ld(a){var b=id();b.update(a);return b.Ra().toLowerCase()}
;var md={};function nd(a){this.h=a||{cookie:""}}
m=nd.prototype;m.isEnabled=function(){if(!y.navigator.cookieEnabled)return!1;if(!this.isEmpty())return!0;this.set("TESTCOOKIESENABLED","1",{ya:60});if("1"!==this.get("TESTCOOKIESENABLED"))return!1;this.remove("TESTCOOKIESENABLED");return!0};
m.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.Tl;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.ya}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);this.h.cookie=a+"="+b+(f?";domain="+f:"")+(g?";path="+g:"")+(0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Date.now()+1E3*h)).toUTCString())+(d?";secure":"")+(null!=e?";samesite="+e:"")};
m.get=function(a,b){for(var c=a+"=",d=(this.h.cookie||"").split(";"),e=0,f;e<d.length;e++){f=zb(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
m.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{ya:0,path:b,domain:c});return d};
m.isEmpty=function(){return!this.h.cookie};
m.clear=function(){for(var a=(this.h.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=zb(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var od=new nd("undefined"==typeof document?null:document);function pd(a){return!!md.FPA_SAMESITE_PHASE2_MOD||!(void 0===a||!a)}
function qd(a){a=void 0===a?!1:a;var b=y.__SAPISID||y.__APISID||y.__3PSAPISID||y.__OVERRIDE_SID;pd(a)&&(b=b||y.__1PSAPISID);if(b)return!0;var c=new nd(document);b=c.get("SAPISID")||c.get("APISID")||c.get("__Secure-3PAPISID")||c.get("SID");pd(a)&&(b=b||c.get("__Secure-1PAPISID"));return!!b}
function rd(a,b,c,d){(a=y[a])||(a=(new nd(document)).get(b));return a?jd(a,c,d):null}
function sd(a){var b=void 0===b?!1:b;var c=hd(String(y.location.href)),d=[];if(qd(b)){c=0==c.indexOf("https:")||0==c.indexOf("chrome-extension:")||0==c.indexOf("moz-extension:");var e=c?y.__SAPISID:y.__APISID;e||(e=new nd(document),e=e.get(c?"SAPISID":"APISID")||e.get("__Secure-3PAPISID"));(e=e?jd(e,c?"SAPISIDHASH":"APISIDHASH",a):null)&&d.push(e);c&&pd(b)&&((b=rd("__1PSAPISID","__Secure-1PAPISID","SAPISID1PHASH",a))&&d.push(b),(a=rd("__3PSAPISID","__Secure-3PAPISID","SAPISID3PHASH",a))&&d.push(a))}return 0==
d.length?null:d.join(" ")}
;function td(){this.data_=[];this.h=-1}
td.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&0===a%1&&this.data_[a]!=b&&(this.data_[a]=b,this.h=-1)};
td.prototype.get=function(a){return!!this.data_[a]};
function ud(a){-1==a.h&&(a.h=Za(a.data_,function(b,c,d){return c?b+Math.pow(2,d):b},0));
return a.h}
;function vd(a,b){this.j=a;this.l=b;this.i=0;this.h=null}
vd.prototype.get=function(){if(0<this.i){this.i--;var a=this.h;this.h=a.next;a.next=null}else a=this.j();return a};
function wd(a,b){a.l(b);100>a.i&&(a.i++,b.next=a.h,a.h=b)}
;var xd;
function yd(){var a=y.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!G("Presto")&&(a=function(){var e=Vc(document,"IFRAME");e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=Pa(function(k){if(("*"==h||k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!G("Trident")&&!G("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.Ea;c.Ea=null;e()}};
return function(e){d.next={Ea:e};d=d.next;b.port2.postMessage(0)}}return function(e){y.setTimeout(e,0)}}
;function zd(a){y.setTimeout(function(){throw a;},0)}
;function Ad(){this.i=this.h=null}
Ad.prototype.add=function(a,b){var c=Bd.get();c.set(a,b);this.i?this.i.next=c:this.h=c;this.i=c};
Ad.prototype.remove=function(){var a=null;this.h&&(a=this.h,this.h=this.h.next,this.h||(this.i=null),a.next=null);return a};
var Bd=new vd(function(){return new Cd},function(a){return a.reset()});
function Cd(){this.next=this.scope=this.h=null}
Cd.prototype.set=function(a,b){this.h=a;this.scope=b;this.next=null};
Cd.prototype.reset=function(){this.next=this.scope=this.h=null};function Dd(a,b){Ed||Fd();Gd||(Ed(),Gd=!0);Hd.add(a,b)}
var Ed;function Fd(){if(y.Promise&&y.Promise.resolve){var a=y.Promise.resolve(void 0);Ed=function(){a.then(Id)}}else Ed=function(){var b=Id;
"function"!==typeof y.setImmediate||y.Window&&y.Window.prototype&&!G("Edge")&&y.Window.prototype.setImmediate==y.setImmediate?(xd||(xd=yd()),xd(b)):y.setImmediate(b)}}
var Gd=!1,Hd=new Ad;function Id(){for(var a;a=Hd.remove();){try{a.h.call(a.scope)}catch(b){zd(b)}wd(Bd,a)}Gd=!1}
;function Jd(a,b){this.i=a[y.Symbol.iterator]();this.j=b;this.l=0}
Jd.prototype[Symbol.iterator]=function(){return this};
Jd.prototype.next=function(){var a=this.i.next();return{value:a.done?void 0:this.j.call(void 0,a.value,this.l++),done:a.done}};
function Kd(a,b){return new Jd(a,b)}
;function Ld(){this.blockSize=-1}
;function Md(){this.blockSize=-1;this.blockSize=64;this.h=[];this.u=[];this.m=[];this.j=[];this.j[0]=128;for(var a=1;a<this.blockSize;++a)this.j[a]=0;this.l=this.i=0;this.reset()}
C(Md,Ld);Md.prototype.reset=function(){this.h[0]=1732584193;this.h[1]=4023233417;this.h[2]=2562383102;this.h[3]=271733878;this.h[4]=3285377520;this.l=this.i=0};
function Nd(a,b,c){c||(c=0);var d=a.m;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.h[0];c=a.h[1];var g=a.h[2],h=a.h[3],k=a.h[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.h[0]=a.h[0]+b&4294967295;a.h[1]=a.h[1]+c&4294967295;a.h[2]=a.h[2]+g&4294967295;a.h[3]=a.h[3]+h&4294967295;a.h[4]=a.h[4]+k&4294967295}
Md.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.blockSize,d=0,e=this.u,f=this.i;d<b;){if(0==f)for(;d<=c;)Nd(this,a,d),d+=this.blockSize;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.blockSize){Nd(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.blockSize){Nd(this,e);f=0;break}}this.i=f;this.l+=b}};
Md.prototype.digest=function(){var a=[],b=8*this.l;56>this.i?this.update(this.j,56-this.i):this.update(this.j,this.blockSize-(this.i-56));for(var c=this.blockSize-1;56<=c;c--)this.u[c]=b&255,b/=256;Nd(this,this.u);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.h[c]>>d&255,++b;return a};function Od(a){var b=B("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(g){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||y.$googDebugFname||b}catch(g){e="Not available",c=!0}b=Pd(a);if(!(!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){c=a.message;if(null==
c){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)c=a.constructor.name;else if(c=a.constructor,Qd[c])c=Qd[c];else{c=String(c);if(!Qd[c]){var f=/function\s+([^\(]+)/m.exec(c);Qd[c]=f?f[1]:"[Anonymous]"}c=Qd[c]}c='Unknown Error of type "'+c+'"'}else c="Unknown Error of unknown type";"function"===typeof a.toString&&Object.prototype.toString!==a.toString&&(c+=": "+a.toString())}return{message:c,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:b||"Not available"}}a.stack=
b;return{message:a.message,name:a.name,lineNumber:a.lineNumber,fileName:a.fileName,stack:a.stack}}
function Pd(a,b){b||(b={});b[Rd(a)]=!0;var c=a.stack||"";(a=a.Qa)&&!b[Rd(a)]&&(c+="\nCaused by: ",a.stack&&0==a.stack.indexOf(a.toString())||(c+="string"===typeof a?a:a.message+"\n"),c+=Pd(a,b));return c}
function Rd(a){var b="";"function"===typeof a.toString&&(b=""+a);return b+a.stack}
var Qd={};function Sd(a){a&&"function"==typeof a.dispose&&a.dispose()}
;function Td(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];Ha(d)?Td.apply(null,d):Sd(d)}}
;function L(){this.h=this.h;this.u=this.u}
L.prototype.h=!1;L.prototype.dispose=function(){this.h||(this.h=!0,this.D())};
function Ud(a,b){a.h?b():(a.u||(a.u=[]),a.u.push(b))}
L.prototype.D=function(){if(this.u)for(;this.u.length;)this.u.shift()()};function Vd(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}
function Wd(a,b){"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function Xd(a,b){a.classList?b=a.classList.contains(b):(a=a.classList?a.classList:Vd(a).match(/\S+/g)||[],b=0<=Wa(a,b));return b}
function Yd(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):Xd(a,"inverted-hdpi")&&Wd(a,Array.prototype.filter.call(a.classList?a.classList:Vd(a).match(/\S+/g)||[],function(b){return"inverted-hdpi"!=b}).join(" "))}
;var Zd="StopIteration"in y?y.StopIteration:{message:"StopIteration",stack:""};function $d(){}
$d.prototype.next=function(){return $d.prototype.h.call(this)};
$d.prototype.h=function(){throw Zd;};
$d.prototype.J=function(){return this};function ae(a){if(a instanceof be||a instanceof ce||a instanceof de)return a;if("function"==typeof a.next)return new be(function(){return ee(a)});
if("function"==typeof a[Symbol.iterator])return new be(function(){return a[Symbol.iterator]()});
if("function"==typeof a.J)return new be(function(){return ee(a.J())});
throw Error("Not an iterator or iterable.");}
function ee(a){if(!(a instanceof $d))return a;var b=!1;return{next:function(){for(var c;!b;)try{c=a.h();break}catch(d){if(d!==Zd)throw d;b=!0}return{value:c,done:b}}}}
function be(a){this.j=a}
be.prototype.J=function(){return new ce(this.j())};
be.prototype[Symbol.iterator]=function(){return new de(this.j())};
be.prototype.i=function(){return new de(this.j())};
function ce(a){this.j=a}
v(ce,$d);ce.prototype.h=function(){var a=this.j.next();if(a.done)throw Zd;return a.value};
ce.prototype.next=function(){return ce.prototype.h.call(this)};
ce.prototype[Symbol.iterator]=function(){return new de(this.j)};
ce.prototype.i=function(){return new de(this.j)};
function de(a){be.call(this,function(){return a});
this.l=a}
v(de,be);de.prototype.next=function(){return this.l.next()};function fe(a,b){this.i={};this.h=[];this.V=this.size=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof fe)for(c=ge(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function ge(a){he(a);return a.h.concat()}
m=fe.prototype;m.has=function(a){return ie(this.i,a)};
m.equals=function(a,b){if(this===a)return!0;if(this.size!=a.size)return!1;b=b||je;he(this);for(var c,d=0;c=this.h[d];d++)if(!b(this.get(c),a.get(c)))return!1;return!0};
function je(a,b){return a===b}
m.isEmpty=function(){return 0==this.size};
m.clear=function(){this.i={};this.V=this.size=this.h.length=0};
m.remove=function(a){return this.delete(a)};
m.delete=function(a){return ie(this.i,a)?(delete this.i[a],--this.size,this.V++,this.h.length>2*this.size&&he(this),!0):!1};
function he(a){if(a.size!=a.h.length){for(var b=0,c=0;b<a.h.length;){var d=a.h[b];ie(a.i,d)&&(a.h[c++]=d);b++}a.h.length=c}if(a.size!=a.h.length){var e={};for(c=b=0;b<a.h.length;)d=a.h[b],ie(e,d)||(a.h[c++]=d,e[d]=1),b++;a.h.length=c}}
m.get=function(a,b){return ie(this.i,a)?this.i[a]:b};
m.set=function(a,b){ie(this.i,a)||(this.size+=1,this.h.push(a),this.V++);this.i[a]=b};
m.forEach=function(a,b){for(var c=ge(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
m.clone=function(){return new fe(this)};
m.keys=function(){return ae(this.J(!0)).i()};
m.values=function(){return ae(this.J(!1)).i()};
m.entries=function(){var a=this;return Kd(this.keys(),function(b){return[b,a.get(b)]})};
m.J=function(a){he(this);var b=0,c=this.V,d=this,e=new $d;e.h=function(){if(c!=d.V)throw Error("The map has changed since the iterator was created");if(b>=d.h.length)throw Zd;var f=d.h[b++];return a?f:d.i[f]};
e.next=e.h.bind(e);return e};
function ie(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
;function ke(a,b){this.type=a;this.h=this.target=b;this.defaultPrevented=this.j=!1}
ke.prototype.stopPropagation=function(){this.j=!0};
ke.prototype.preventDefault=function(){this.defaultPrevented=!0};var le=function(){if(!y.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
try{y.addEventListener("test",Ea,b),y.removeEventListener("test",Ea,b)}catch(c){}return a}();function me(a,b){ke.call(this,a?a.type:"");this.relatedTarget=this.h=this.target=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=0;this.key="";this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.state=null;this.pointerId=0;this.pointerType="";this.i=null;a&&this.init(a,b)}
C(me,ke);var ne={2:"touch",3:"pen",4:"mouse"};
me.prototype.init=function(a,b){var c=this.type=a.type,d=a.changedTouches&&a.changedTouches.length?a.changedTouches[0]:null;this.target=a.target||a.srcElement;this.h=b;if(b=a.relatedTarget){if(nc){a:{try{jc(b.nodeName);var e=!0;break a}catch(f){}e=!1}e||(b=null)}}else"mouseover"==c?b=a.fromElement:"mouseout"==c&&(b=a.toElement);this.relatedTarget=b;d?(this.clientX=void 0!==d.clientX?d.clientX:d.pageX,this.clientY=void 0!==d.clientY?d.clientY:d.pageY,this.screenX=d.screenX||0,this.screenY=d.screenY||
0):(this.clientX=void 0!==a.clientX?a.clientX:a.pageX,this.clientY=void 0!==a.clientY?a.clientY:a.pageY,this.screenX=a.screenX||0,this.screenY=a.screenY||0);this.button=a.button;this.keyCode=a.keyCode||0;this.key=a.key||"";this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.pointerId=a.pointerId||0;this.pointerType="string"===typeof a.pointerType?a.pointerType:ne[a.pointerType]||"";this.state=a.state;
this.i=a;a.defaultPrevented&&me.L.preventDefault.call(this)};
me.prototype.stopPropagation=function(){me.L.stopPropagation.call(this);this.i.stopPropagation?this.i.stopPropagation():this.i.cancelBubble=!0};
me.prototype.preventDefault=function(){me.L.preventDefault.call(this);var a=this.i;a.preventDefault?a.preventDefault():a.returnValue=!1};var oe="closure_listenable_"+(1E6*Math.random()|0);var pe=0;function qe(a,b,c,d,e){this.listener=a;this.h=null;this.src=b;this.type=c;this.capture=!!d;this.ja=e;this.key=++pe;this.da=this.ga=!1}
function re(a){a.da=!0;a.listener=null;a.h=null;a.src=null;a.ja=null}
;function se(a){this.src=a;this.listeners={};this.h=0}
se.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.listeners[f];a||(a=this.listeners[f]=[],this.h++);var g=te(a,b,d,e);-1<g?(b=a[g],c||(b.ga=!1)):(b=new qe(b,this.src,f,!!d,e),b.ga=c,a.push(b));return b};
se.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.listeners))return!1;var e=this.listeners[a];b=te(e,b,c,d);return-1<b?(re(e[b]),Array.prototype.splice.call(e,b,1),0==e.length&&(delete this.listeners[a],this.h--),!0):!1};
function ue(a,b){var c=b.type;c in a.listeners&&ab(a.listeners[c],b)&&(re(b),0==a.listeners[c].length&&(delete a.listeners[c],a.h--))}
function te(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.da&&f.listener==b&&f.capture==!!c&&f.ja==d)return e}return-1}
;var ve="closure_lm_"+(1E6*Math.random()|0),we={},xe=0;function ye(a,b,c,d,e){if(d&&d.once)ze(a,b,c,d,e);else if(Array.isArray(b))for(var f=0;f<b.length;f++)ye(a,b[f],c,d,e);else c=Ae(c),a&&a[oe]?a.ba(b,c,Ia(d)?!!d.capture:!!d,e):Be(a,b,c,!1,d,e)}
function Be(a,b,c,d,e,f){if(!b)throw Error("Invalid event type");var g=Ia(e)?!!e.capture:!!e,h=Ce(a);h||(a[ve]=h=new se(a));c=h.add(b,c,d,g,f);if(!c.h){d=De();c.h=d;d.src=a;d.listener=c;if(a.addEventListener)le||(e=g),void 0===e&&(e=!1),a.addEventListener(b.toString(),d,e);else if(a.attachEvent)a.attachEvent(Ee(b.toString()),d);else if(a.addListener&&a.removeListener)a.addListener(d);else throw Error("addEventListener and attachEvent are unavailable.");xe++}}
function De(){function a(c){return b.call(a.src,a.listener,c)}
var b=Fe;return a}
function ze(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)ze(a,b[f],c,d,e);else c=Ae(c),a&&a[oe]?a.i.add(String(b),c,!0,Ia(d)?!!d.capture:!!d,e):Be(a,b,c,!0,d,e)}
function Ge(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)Ge(a,b[f],c,d,e);else(d=Ia(d)?!!d.capture:!!d,c=Ae(c),a&&a[oe])?a.i.remove(String(b),c,d,e):a&&(a=Ce(a))&&(b=a.listeners[b.toString()],a=-1,b&&(a=te(b,c,d,e)),(c=-1<a?b[a]:null)&&He(c))}
function He(a){if("number"!==typeof a&&a&&!a.da){var b=a.src;if(b&&b[oe])ue(b.i,a);else{var c=a.type,d=a.h;b.removeEventListener?b.removeEventListener(c,d,a.capture):b.detachEvent?b.detachEvent(Ee(c),d):b.addListener&&b.removeListener&&b.removeListener(d);xe--;(c=Ce(b))?(ue(c,a),0==c.h&&(c.src=null,b[ve]=null)):re(a)}}}
function Ee(a){return a in we?we[a]:we[a]="on"+a}
function Fe(a,b){if(a.da)a=!0;else{b=new me(b,this);var c=a.listener,d=a.ja||a.src;a.ga&&He(a);a=c.call(d,b)}return a}
function Ce(a){a=a[ve];return a instanceof se?a:null}
var Ie="__closure_events_fn_"+(1E9*Math.random()>>>0);function Ae(a){if("function"===typeof a)return a;a[Ie]||(a[Ie]=function(b){return a.handleEvent(b)});
return a[Ie]}
;function Je(){L.call(this);this.i=new se(this);this.I=this;this.o=null}
C(Je,L);Je.prototype[oe]=!0;Je.prototype.addEventListener=function(a,b,c,d){ye(this,a,b,c,d)};
Je.prototype.removeEventListener=function(a,b,c,d){Ge(this,a,b,c,d)};
function Ke(a,b){var c=a.o;if(c){var d=[];for(var e=1;c;c=c.o)d.push(c),++e}a=a.I;c=b.type||b;"string"===typeof b?b=new ke(b,a):b instanceof ke?b.target=b.target||a:(e=b,b=new ke(c,a),nb(b,e));e=!0;if(d)for(var f=d.length-1;!b.j&&0<=f;f--){var g=b.h=d[f];e=Le(g,c,!0,b)&&e}b.j||(g=b.h=a,e=Le(g,c,!0,b)&&e,b.j||(e=Le(g,c,!1,b)&&e));if(d)for(f=0;!b.j&&f<d.length;f++)g=b.h=d[f],e=Le(g,c,!1,b)&&e}
Je.prototype.D=function(){Je.L.D.call(this);if(this.i){var a=this.i,b=0,c;for(c in a.listeners){for(var d=a.listeners[c],e=0;e<d.length;e++)++b,re(d[e]);delete a.listeners[c];a.h--}}this.o=null};
Je.prototype.ba=function(a,b,c,d){return this.i.add(String(a),b,!1,c,d)};
function Le(a,b,c,d){b=a.i.listeners[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&&!g.da&&g.capture==c){var h=g.listener,k=g.ja||g.src;g.ga&&ue(a.i,g);e=!1!==h.call(k,d)&&e}}return e&&!d.defaultPrevented}
;function Me(a){Ne();return yb(a)}
var Ne=Ea;function Oe(a){var b=[];Pe(new Qe,a,b);return b.join("")}
function Qe(){}
function Pe(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),Pe(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),Re(d,c),c.push(":"),Pe(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Re(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Se={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Te=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Re(a,b){b.push('"',a.replace(Te,function(c){var d=Se[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).substr(1),Se[c]=d);return d}),'"')}
;function Ue(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function Ve(a){this.h=0;this.o=void 0;this.l=this.i=this.j=null;this.u=this.m=!1;if(a!=Ea)try{var b=this;a.call(void 0,function(c){We(b,2,c)},function(c){We(b,3,c)})}catch(c){We(this,3,c)}}
function Xe(){this.next=this.context=this.onRejected=this.i=this.h=null;this.j=!1}
Xe.prototype.reset=function(){this.context=this.onRejected=this.i=this.h=null;this.j=!1};
var Ye=new vd(function(){return new Xe},function(a){a.reset()});
function Ze(a,b,c){var d=Ye.get();d.i=a;d.onRejected=b;d.context=c;return d}
function $e(a){return new Ve(function(b,c){c(a)})}
Ve.prototype.then=function(a,b,c){return af(this,"function"===typeof a?a:null,"function"===typeof b?b:null,c)};
Ve.prototype.$goog_Thenable=!0;function bf(a,b){return af(a,null,b,void 0)}
Ve.prototype.cancel=function(a){if(0==this.h){var b=new cf(a);Dd(function(){df(this,b)},this)}};
function df(a,b){if(0==a.h)if(a.j){var c=a.j;if(c.i){for(var d=0,e=null,f=null,g=c.i;g&&(g.j||(d++,g.h==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.h&&1==d?df(c,b):(f?(d=f,d.next==c.l&&(c.l=d),d.next=d.next.next):ef(c),ff(c,e,3,b)))}a.j=null}else We(a,3,b)}
function gf(a,b){a.i||2!=a.h&&3!=a.h||hf(a);a.l?a.l.next=b:a.i=b;a.l=b}
function af(a,b,c,d){var e=Ze(null,null,null);e.h=new Ve(function(f,g){e.i=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.onRejected=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof cf?g(h):f(k)}catch(l){g(l)}}:g});
e.h.j=a;gf(a,e);return e.h}
Ve.prototype.C=function(a){this.h=0;We(this,2,a)};
Ve.prototype.F=function(a){this.h=0;We(this,3,a)};
function We(a,b,c){if(0==a.h){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.h=1;a:{var d=c,e=a.C,f=a.F;if(d instanceof Ve){gf(d,Ze(e||Ea,f||null,a));var g=!0}else if(Ue(d))d.then(e,f,a),g=!0;else{if(Ia(d))try{var h=d.then;if("function"===typeof h){jf(d,h,e,f,a);g=!0;break a}}catch(k){f.call(a,k);g=!0;break a}g=!1}}g||(a.o=c,a.h=b,a.j=null,hf(a),3!=b||c instanceof cf||kf(a,c))}}
function jf(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function hf(a){a.m||(a.m=!0,Dd(a.A,a))}
function ef(a){var b=null;a.i&&(b=a.i,a.i=b.next,b.next=null);a.i||(a.l=null);return b}
Ve.prototype.A=function(){for(var a;a=ef(this);)ff(this,a,this.h,this.o);this.m=!1};
function ff(a,b,c,d){if(3==c&&b.onRejected&&!b.j)for(;a&&a.u;a=a.j)a.u=!1;if(b.h)b.h.j=null,lf(b,c,d);else try{b.j?b.i.call(b.context):lf(b,c,d)}catch(e){mf.call(null,e)}wd(Ye,b)}
function lf(a,b,c){2==b?a.i.call(a.context,c):a.onRejected&&a.onRejected.call(a.context,c)}
function kf(a,b){a.u=!0;Dd(function(){a.u&&mf.call(null,b)})}
var mf=zd;function cf(a){Ta.call(this,a)}
C(cf,Ta);cf.prototype.name="cancel";function M(a){L.call(this);this.o=1;this.l=[];this.m=0;this.i=[];this.j={};this.A=!!a}
C(M,L);m=M.prototype;m.subscribe=function(a,b,c){var d=this.j[a];d||(d=this.j[a]=[]);var e=this.o;this.i[e]=a;this.i[e+1]=b;this.i[e+2]=c;this.o=e+3;d.push(e);return e};
function nf(a,b,c,d){if(b=a.j[b]){var e=a.i;(b=b.find(function(f){return e[f+1]==c&&e[f+2]==d}))&&a.ca(b)}}
m.ca=function(a){var b=this.i[a];if(b){var c=this.j[b];0!=this.m?(this.l.push(a),this.i[a+1]=Ea):(c&&ab(c,a),delete this.i[a],delete this.i[a+1],delete this.i[a+2])}return!!b};
m.W=function(a,b){var c=this.j[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.A)for(e=0;e<c.length;e++){var g=c[e];of(this.i[g+1],this.i[g+2],d)}else{this.m++;try{for(e=0,f=c.length;e<f&&!this.h;e++)g=c[e],this.i[g+1].apply(this.i[g+2],d)}finally{if(this.m--,0<this.l.length&&0==this.m)for(;c=this.l.pop();)this.ca(c)}}return 0!=e}return!1};
function of(a,b,c){Dd(function(){a.apply(b,c)})}
m.clear=function(a){if(a){var b=this.j[a];b&&(b.forEach(this.ca,this),delete this.j[a])}else this.i.length=0,this.j={}};
m.D=function(){M.L.D.call(this);this.clear();this.l.length=0};function pf(a){this.h=a}
pf.prototype.set=function(a,b){void 0===b?this.h.remove(a):this.h.set(a,Oe(b))};
pf.prototype.get=function(a){try{var b=this.h.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
pf.prototype.remove=function(a){this.h.remove(a)};function qf(a){this.h=a}
C(qf,pf);function rf(a){this.data=a}
function sf(a){return void 0===a||a instanceof rf?a:new rf(a)}
qf.prototype.set=function(a,b){qf.L.set.call(this,a,sf(b))};
qf.prototype.i=function(a){a=qf.L.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
qf.prototype.get=function(a){if(a=this.i(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function tf(a){this.h=a}
C(tf,qf);tf.prototype.set=function(a,b,c){if(b=sf(b)){if(c){if(c<Date.now()){tf.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Date.now()}tf.L.set.call(this,a,b)};
tf.prototype.i=function(a){var b=tf.L.i.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Date.now()||c&&c>Date.now())tf.prototype.remove.call(this,a);else return b}};function uf(){}
;function vf(){}
C(vf,uf);vf.prototype[Symbol.iterator]=function(){return ae(this.J(!0)).i()};
vf.prototype.clear=function(){var a=Array.from(this);a=u(a);for(var b=a.next();!b.done;b=a.next())this.remove(b.value)};function wf(a){this.h=a}
C(wf,vf);m=wf.prototype;m.isAvailable=function(){if(!this.h)return!1;try{return this.h.setItem("__sak","1"),this.h.removeItem("__sak"),!0}catch(a){return!1}};
m.set=function(a,b){try{this.h.setItem(a,b)}catch(c){if(0==this.h.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
m.get=function(a){a=this.h.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){this.h.removeItem(a)};
m.J=function(a){var b=0,c=this.h,d=new $d;d.h=function(){if(b>=c.length)throw Zd;var e=c.key(b++);if(a)return e;e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
d.next=d.h.bind(d);return d};
m.clear=function(){this.h.clear()};
m.key=function(a){return this.h.key(a)};function xf(){var a=null;try{a=window.localStorage||null}catch(b){}this.h=a}
C(xf,wf);function yf(a,b){this.i=a;this.h=null;var c;if(c=lc)c=!(9<=Number(yc));if(c){zf||(zf=new fe);this.h=zf.get(a);this.h||(b?this.h=document.getElementById(b):(this.h=document.createElement("userdata"),this.h.addBehavior("#default#userData"),document.body.appendChild(this.h)),zf.set(a,this.h));try{this.h.load(this.i)}catch(d){this.h=null}}}
C(yf,vf);var Af={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},zf=null;function Bf(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return Af[b]})}
m=yf.prototype;m.isAvailable=function(){return!!this.h};
m.set=function(a,b){this.h.setAttribute(Bf(a),b);Cf(this)};
m.get=function(a){a=this.h.getAttribute(Bf(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){this.h.removeAttribute(Bf(a));Cf(this)};
m.J=function(a){var b=0,c=this.h.XMLDocument.documentElement.attributes,d=new $d;d.h=function(){if(b>=c.length)throw Zd;var e=c[b++];if(a)return decodeURIComponent(e.nodeName.replace(/\./g,"%")).substr(1);e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
d.next=d.h.bind(d);return d};
m.clear=function(){for(var a=this.h.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);Cf(this)};
function Cf(a){try{a.h.save(a.i)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function Df(a,b){this.i=a;this.h=b+"::"}
C(Df,vf);Df.prototype.set=function(a,b){this.i.set(this.h+a,b)};
Df.prototype.get=function(a){return this.i.get(this.h+a)};
Df.prototype.remove=function(a){this.i.remove(this.h+a)};
Df.prototype.J=function(a){var b=this.i.J(!0),c=this,d=new $d;d.h=function(){for(var e=b.h();e.substr(0,c.h.length)!=c.h;)e=b.h();return a?e.substr(c.h.length):c.i.get(e)};
d.next=d.h.bind(d);return d};function Ef(a,b){1<b.length?a[b[0]]=b[1]:1===b.length&&Object.assign(a,b[0])}
;var Ff,Gf,Hf=y.window,If=(null===(Ff=null===Hf||void 0===Hf?void 0:Hf.yt)||void 0===Ff?void 0:Ff.config_)||(null===(Gf=null===Hf||void 0===Hf?void 0:Hf.ytcfg)||void 0===Gf?void 0:Gf.data_)||{};A("yt.config_",If,void 0);function N(a){for(var b=0;b<arguments.length;++b);Ef(If,arguments)}
function F(a,b){return a in If?If[a]:b}
;var Jf=[];function Kf(a){Jf.forEach(function(b){return b(a)})}
function Lf(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Mf(b)}}:a}
function Mf(a){var b=B("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0):(b=F("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0]),N("ERRORS",b));Kf(a)}
function Nf(a){var b=B("yt.logging.errors.log");b?b(a,"WARNING",void 0,void 0,void 0):(b=F("ERRORS",[]),b.push([a,"WARNING",void 0,void 0,void 0]),N("ERRORS",b))}
;var Of=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};A("yt.msgs_",Of,void 0);function Pf(a){Ef(Of,arguments)}
;function O(a){a=Qf(a);return"string"===typeof a&&"false"===a?!1:!!a}
function Rf(a,b){a=Qf(a);return void 0===a&&void 0!==b?b:Number(a||0)}
function Qf(a){var b=F("EXPERIMENTS_FORCED_FLAGS",{});return void 0!==b[a]?b[a]:F("EXPERIMENT_FLAGS",{})[a]}
;var Sf=0,Tf=oc?"webkit":nc?"moz":lc?"ms":kc?"o":"";A("ytDomDomGetNextId",B("ytDomDomGetNextId")||function(){return++Sf},void 0);var Uf={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function Vf(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.rotation=this.clientY=this.clientX=0;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in Uf||(this[b]=a[b]);this.rotation=a.rotation;var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;if(d)try{d=d.nodeName?
d:null}catch(e){d=null}else"mouseover"==this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.h=a.pageX;this.i=a.pageY}}catch(e){}}
function Wf(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.h=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.i=a.clientY+b}}
Vf.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
Vf.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
Vf.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var fb=y.ytEventsEventsListeners||{};A("ytEventsEventsListeners",fb,void 0);var Xf=y.ytEventsEventsCounter||{count:0};A("ytEventsEventsCounter",Xf,void 0);
function Yf(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return eb(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Ia(e[4])&&Ia(d)&&jb(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
var Zf=Va(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function $f(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=Yf(a,b,c,d);if(e)return e;e=++Xf.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new Vf(h);if(!Xc(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new Vf(h);
h.currentTarget=a;return c.call(a,h)};
g=Lf(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),Zf()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);fb[e]=[a,b,c,g,d];return e}
function ag(a){a&&("string"==typeof a&&(a=[a]),D(a,function(b){if(b in fb){var c=fb[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?Zf()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete fb[b]}}))}
;var bg=window.ytcsi&&window.ytcsi.now?window.ytcsi.now:window.performance&&window.performance.timing&&window.performance.now&&window.performance.timing.navigationStart?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};function cg(a,b){"function"===typeof a&&(a=Lf(a));return window.setTimeout(a,b)}
function dg(a){window.clearTimeout(a)}
;function eg(a){this.C=a;this.i=null;this.m=0;this.A=null;this.o=0;this.j=[];for(a=0;4>a;a++)this.j.push(0);this.l=0;this.I=$f(window,"mousemove",Pa(this.M,this));a=Pa(this.F,this);"function"===typeof a&&(a=Lf(a));this.N=window.setInterval(a,25)}
C(eg,L);eg.prototype.M=function(a){void 0===a.h&&Wf(a);var b=a.h;void 0===a.i&&Wf(a);this.i=new Pc(b,a.i)};
eg.prototype.F=function(){if(this.i){var a=bg();if(0!=this.m){var b=this.A,c=this.i,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.m);this.j[this.l]=.5<Math.abs((d-this.o)/this.o)?1:0;for(c=b=0;4>c;c++)b+=this.j[c]||0;3<=b&&this.C();this.o=d}this.m=a;this.A=this.i;this.l=(this.l+1)%4}};
eg.prototype.D=function(){window.clearInterval(this.N);ag(this.I)};function fg(){}
function gg(a,b){return hg(a,0,b)}
function ig(a,b){return hg(a,1,b)}
;function jg(){fg.apply(this,arguments)}
v(jg,fg);function hg(a,b,c){void 0!==c&&Number.isNaN(Number(c))&&(c=void 0);var d=B("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):cg(a,c||0)}
function kg(a){if(void 0===a||!Number.isNaN(Number(a))){var b=B("yt.scheduler.instance.cancelJob");b?b(a):dg(a)}}
jg.prototype.start=function(){var a=B("yt.scheduler.instance.start");a&&a()};
jg.prototype.pause=function(){var a=B("yt.scheduler.instance.pause");a&&a()};jg.h||(jg.h=new jg);var lg={};
function mg(a){var b=void 0===a?{}:a;a=void 0===b.kb?!1:b.kb;b=void 0===b.Ua?!0:b.Ua;if(null==B("_lact",window)){var c=parseInt(F("LACT"),10);c=isFinite(c)?Date.now()-Math.max(c,0):-1;A("_lact",c,window);A("_fact",c,window);-1==c&&ng();$f(document,"keydown",ng);$f(document,"keyup",ng);$f(document,"mousedown",ng);$f(document,"mouseup",ng);a?$f(window,"touchmove",function(){og("touchmove",200)},{passive:!0}):($f(window,"resize",function(){og("resize",200)}),b&&$f(window,"scroll",function(){og("scroll",200)}));
new eg(function(){og("mouse",100)});
$f(document,"touchstart",ng,{passive:!0});$f(document,"touchend",ng,{passive:!0})}}
function og(a,b){lg[a]||(lg[a]=!0,ig(function(){ng();lg[a]=!1},b))}
function ng(){null==B("_lact",window)&&mg();var a=Date.now();A("_lact",a,window);-1==B("_fact",window)&&A("_fact",a,window);(a=B("ytglobal.ytUtilActivityCallback_"))&&a()}
function pg(){var a=B("_lact",window);return null==a?-1:Math.max(Date.now()-a,0)}
;function qg(){var a=rg;B("yt.ads.biscotti.getId_")||A("yt.ads.biscotti.getId_",a,void 0)}
function sg(a){A("yt.ads.biscotti.lastId_",a,void 0)}
;var tg=/^[\w.]*$/,ug={q:!0,search_query:!0};function vg(a,b){b=a.split(b);for(var c={},d=0,e=b.length;d<e;d++){var f=b[d].split("=");if(1==f.length&&f[0]||2==f.length)try{var g=wg(f[0]||""),h=wg(f[1]||"");g in c?Array.isArray(c[g])?cb(c[g],h):c[g]=[c[g],h]:c[g]=h}catch(q){var k=q,l=f[0],n=String(vg);k.args=[{key:l,value:f[1],query:a,method:xg==n?"unchanged":n}];ug.hasOwnProperty(l)||Nf(k)}}return c}
var xg=String(vg);function yg(a){var b=[];db(a,function(c,d){var e=encodeURIComponent(String(d)),f;Array.isArray(c)?f=c:f=[c];D(f,function(g){""==g?b.push(e):b.push(e+"="+encodeURIComponent(String(g)))})});
return b.join("&")}
function zg(a){"?"==a.charAt(0)&&(a=a.substr(1));return vg(a,"&")}
function Ag(){var a=window.location.href;return-1!=a.indexOf("?")?(a=(a||"").split("#")[0],a=a.split("?",2),zg(1<a.length?a[1]:a[0])):{}}
function Bg(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=zg(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);return gc(a,e)+d}
function Cg(a){if(!b)var b=window.location.href;var c=a.match(bc)[1]||null,d=dc(a);c&&d?(a=a.match(bc),b=b.match(bc),a=a[3]==b[3]&&a[1]==b[1]&&a[4]==b[4]):a=d?dc(b)==d&&(Number(b.match(bc)[4]||null)||null)==(Number(a.match(bc)[4]||null)||null):!0;return a}
function wg(a){return a&&a.match(tg)?a:decodeURIComponent(a.replace(/\+/g," "))}
;function Dg(a){var b=Eg;a=void 0===a?B("yt.ads.biscotti.lastId_")||"":a;var c=Object,d=c.assign,e={};e.dt=gd;e.flash="0";a:{try{var f=b.h.top.location.href}catch(Ja){f=2;break a}f=f?f===b.i.location.href?0:1:2}e=(e.frm=f,e);try{e.u_tz=-(new Date).getTimezoneOffset();var g=void 0===g?K:g;try{var h=g.history.length}catch(Ja){h=0}e.u_his=h;e.u_java=!!K.navigator&&"unknown"!==typeof K.navigator.javaEnabled&&!!K.navigator.javaEnabled&&K.navigator.javaEnabled();K.screen&&(e.u_h=K.screen.height,e.u_w=K.screen.width,
e.u_ah=K.screen.availHeight,e.u_aw=K.screen.availWidth,e.u_cd=K.screen.colorDepth);K.navigator&&K.navigator.plugins&&(e.u_nplug=K.navigator.plugins.length);K.navigator&&K.navigator.mimeTypes&&(e.u_nmime=K.navigator.mimeTypes.length)}catch(Ja){}h=b.h;try{var k=h.screenX;var l=h.screenY}catch(Ja){}try{var n=h.outerWidth;var q=h.outerHeight}catch(Ja){}try{var r=h.innerWidth;var p=h.innerHeight}catch(Ja){}try{var z=h.screenLeft;var I=h.screenTop}catch(Ja){}try{r=h.innerWidth,p=h.innerHeight}catch(Ja){}try{var E=
h.screen.availWidth;var R=h.screen.availTop}catch(Ja){}k=[z,I,k,l,E,R,n,q,r,p];l=b.h.top;try{var V=(l||window).document,J="CSS1Compat"==V.compatMode?V.documentElement:V.body;var U=(new Qc(J.clientWidth,J.clientHeight)).round()}catch(Ja){U=new Qc(-12245933,-12245933)}V=U;U={};J=new td;y.SVGElement&&y.document.createElementNS&&J.set(0);l=bd();l["allow-top-navigation-by-user-activation"]&&J.set(1);l["allow-popups-to-escape-sandbox"]&&J.set(2);y.crypto&&y.crypto.subtle&&J.set(3);y.TextDecoder&&y.TextEncoder&&
J.set(4);J=ud(J);U.bc=J;U.bih=V.height;U.biw=V.width;U.brdim=k.join();b=b.i;b=(U.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[b.visibilityState||b.webkitVisibilityState||b.mozVisibilityState||""]||0,U.wgl=!!K.WebGLRenderingContext,U);c=d.call(c,e,b);c.ca_type="image";a&&(c.bid=a);return c}
var Eg=new function(){var a=window.document;this.h=window;this.i=a};
A("yt.ads_.signals_.getAdSignalsString",function(a){return yg(Dg(a))},void 0);var Fg="XMLHttpRequest"in y?function(){return new XMLHttpRequest}:null;
function Gg(){if(!Fg)return null;var a=Fg();return"open"in a?a:null}
function Hg(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;var Ig={Authorization:"AUTHORIZATION","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-Youtube-Domain-Admin-State":"DOMAIN_ADMIN_STATE","X-Youtube-Chrome-Connected":"CHROME_CONNECTED_HEADER","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Delegation-Context":"INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL",
"X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},Jg="app debugcss debugjs expflag force_ad_params force_ad_encrypted force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address".split(" ").concat(fa("client_dev_mss_url client_dev_regex_map client_dev_root_url expflag jsfeat jsmode client_rollout_override".split(" "))),Kg=!1;
function Lg(a,b){b=void 0===b?{}:b;var c=Cg(a),d=O("web_ajax_ignore_global_headers_if_set"),e;for(e in Ig){var f=F(Ig[e]);!f||!c&&dc(a)||d&&void 0!==b[e]||(b[e]=f)}if(c||!dc(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());if(c||!dc(a)){try{var g=(new Intl.DateTimeFormat).resolvedOptions().timeZone}catch(h){}g&&(b["X-YouTube-Time-Zone"]=g)}if(c||!dc(a))b["X-YouTube-Ad-Signals"]=yg(Dg(void 0));return b}
function Mg(a){var b=window.location.search,c=dc(a);O("debug_handle_relative_url_for_query_forward_killswitch")||c||!Cg(a)||(c=document.location.hostname);var d=cc(a.match(bc)[5]||null);d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=zg(b),f={};D(Jg,function(g){e[g]&&(f[g]=e[g])});
return Bg(a,f||{},!1)}
function Ng(a,b){var c=b.format||"JSON";a=Og(a,b);var d=Pg(a,b),e=!1,f=Qg(a,function(k){if(!e){e=!0;h&&dg(h);var l=Hg(k),n=null,q=400<=k.status&&500>k.status,r=500<=k.status&&600>k.status;if(l||q||r)n=Rg(a,c,k,b.convertToSafeHtml);if(l)a:if(k&&204==k.status)l=!0;else{switch(c){case "XML":l=0==parseInt(n&&n.return_code,10);break a;case "RAW":l=!0;break a}l=!!n}n=n||{};q=b.context||y;l?b.onSuccess&&b.onSuccess.call(q,k,n):b.onError&&b.onError.call(q,k,n);b.onFinish&&b.onFinish.call(q,k,n)}},b.method,
d,b.headers,b.responseType,b.withCredentials);
if(b.onTimeout&&0<b.timeout){var g=b.onTimeout;var h=cg(function(){e||(e=!0,f.abort(),dg(h),g.call(b.context||y,f))},b.timeout)}return f}
function Og(a,b){b.includeDomain&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=F("XSRF_FIELD_NAME",void 0);if(b=b.urlParams)b[c]&&delete b[c],a=Bg(a,b||{},!0);return a}
function Pg(a,b){var c=F("XSRF_FIELD_NAME",void 0),d=F("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.postParams,g=F("XSRF_FIELD_NAME",void 0),h;b.headers&&(h=b.headers["Content-Type"]);b.excludeXsrf||dc(a)&&!b.withCredentials&&dc(a)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.postParams&&b.postParams[g]||(f||(f={}),f[c]=d);f&&"string"===typeof e&&(e=zg(e),nb(e,f),e=b.postBodyFormat&&"JSON"==b.postBodyFormat?JSON.stringify(e):fc(e));f=e||f&&!gb(f);!Kg&&f&&
"POST"!=b.method&&(Kg=!0,Mf(Error("AJAX request with postData should use POST")));return e}
function Rg(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,Nf(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(")]}'\n"===f.substring(0,5)&&(f=f.substring(5)),e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?Sg(a):null)e={},D(a.getElementsByTagName("*"),function(g){e[g.tagName]=Tg(g)})}d&&Ug(e);
return e}
function Ug(a){if(Ia(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;sb("HTML that is escaped and sanitized server-side and passed through yt.net.ajax");var d=Vb(a[b],null);a[c]=d}else Ug(a[b])}}
function Sg(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Tg(a){var b="";D(a.childNodes,function(c){b+=c.nodeValue});
return b}
function Qg(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&Lf(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=Gg();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;O("debug_forward_web_query_parameters")&&(a=Mg(a));k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=Lg(a,e))for(var l in e)k.setRequestHeader(l,e[l]),"content-type"==l.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);
return k}
;var Vg=zc||Ac;function Wg(a){var b=Ob;return b?0<=b.toLowerCase().indexOf(a):!1}
;var Xg={},Yg=0;
function Zg(a,b,c,d,e){e=void 0===e?"":e;if(a)if(c&&!Wg("cobalt")){if(a){a instanceof Hb||(a="object"==typeof a&&a.R?a.P():String(a),Mb.test(a)?a=new Hb(a,Ib):(a=String(a),a=a.replace(/(%0A|%0D)/g,""),a=(b=a.match(Lb))&&Kb.test(b[1])?new Hb(a,Ib):null));b=Jb(a||Nb);if("about:invalid#zClosurez"===b||b.startsWith("data"))a="";else{if(b instanceof Ub)a=b;else{var f="object"==typeof b;a=null;f&&b.wa&&(a=b.ra());b=f&&b.R?b.P():String(b);Gb.test(b)&&(-1!=b.indexOf("&")&&(b=b.replace(Ab,"&amp;")),-1!=b.indexOf("<")&&
(b=b.replace(Bb,"&lt;")),-1!=b.indexOf(">")&&(b=b.replace(Cb,"&gt;")),-1!=b.indexOf('"')&&(b=b.replace(Db,"&quot;")),-1!=b.indexOf("'")&&(b=b.replace(Eb,"&#39;")),-1!=b.indexOf("\x00")&&(b=b.replace(Fb,"&#0;")));a=Vb(b,a)}a instanceof Ub&&a.constructor===Ub?a=a.h:(Ga(a),a="type_error:SafeHtml");a=encodeURIComponent(String(Oe(a.toString())))}/^[\s\xa0]*$/.test(a)||(a=Uc("IFRAME",{src:'javascript:"<body><img src=\\""+'+a+'+"\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a))}}else if(e)Qg(a,
b,"POST",e,d);else if(F("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d)Qg(a,b,"GET","",d);else{b:{try{var g=new Ua({url:a});if(g.j&&g.i||g.l){var h=cc(a.match(bc)[5]||null),k;if(!(k=!h||!h.endsWith("/aclk"))){var l=a.search(hc);d:{for(c=0;0<=(c=a.indexOf("ri",c))&&c<l;){var n=a.charCodeAt(c-1);if(38==n||63==n){var q=a.charCodeAt(c+2);if(!q||61==q||38==q||35==q){var r=c;break d}}c+=3}r=-1}if(0>r)var p=null;else{var z=a.indexOf("&",r);if(0>z||z>l)z=l;r+=3;p=decodeURIComponent(a.substr(r,z-r).replace(/\+/g,
" "))}k="1"!==p}f=!k;break b}}catch(I){}f=!1}f?$g(a)?(b&&b(),f=!0):f=!1:f=!1;f||ah(a,b)}}
function bh(a,b,c){c=void 0===c?"":c;$g(a,c)?b&&b():Zg(a,b,void 0,void 0,c)}
function $g(a,b){try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,void 0===b?"":b))return!0}catch(c){}return!1}
function ah(a,b){var c=new Image,d=""+Yg++;Xg[d]=c;c.onload=c.onerror=function(){b&&Xg[d]&&b();delete Xg[d]};
c.src=a}
;var ch=y.ytPubsubPubsubInstance||new M,dh=y.ytPubsubPubsubSubscribedKeys||{},eh=y.ytPubsubPubsubTopicToKeys||{},fh=y.ytPubsubPubsubIsSynchronous||{};function gh(a,b){var c=hh();if(c&&b){var d=c.subscribe(a,function(){var e=arguments;var f=function(){dh[d]&&b.apply&&"function"==typeof b.apply&&b.apply(window,e)};
try{fh[a]?f():cg(f,0)}catch(g){Mf(g)}},void 0);
dh[d]=!0;eh[a]||(eh[a]=[]);eh[a].push(d);return d}return 0}
function ih(a){var b=hh();b&&("number"===typeof a?a=[a]:"string"===typeof a&&(a=[parseInt(a,10)]),D(a,function(c){b.unsubscribeByKey(c);delete dh[c]}))}
function jh(a,b){var c=hh();c&&c.publish.apply(c,arguments)}
function kh(a){var b=hh();if(b)if(b.clear(a),a)lh(a);else for(var c in eh)lh(c)}
function hh(){return y.ytPubsubPubsubInstance}
function lh(a){eh[a]&&(a=eh[a],D(a,function(b){dh[b]&&delete dh[b]}),a.length=0)}
M.prototype.subscribe=M.prototype.subscribe;M.prototype.unsubscribeByKey=M.prototype.ca;M.prototype.publish=M.prototype.W;M.prototype.clear=M.prototype.clear;A("ytPubsubPubsubInstance",ch,void 0);A("ytPubsubPubsubTopicToKeys",eh,void 0);A("ytPubsubPubsubIsSynchronous",fh,void 0);A("ytPubsubPubsubSubscribedKeys",dh,void 0);var mh=window,P=mh.ytcsi&&mh.ytcsi.now?mh.ytcsi.now:mh.performance&&mh.performance.timing&&mh.performance.now&&mh.performance.timing.navigationStart?function(){return mh.performance.timing.navigationStart+mh.performance.now()}:function(){return(new Date).getTime()};var nh=Rf("initial_gel_batch_timeout",2E3),oh=Math.pow(2,16)-1,ph=null,qh=0,rh=void 0,sh=0,th=0,uh=0,vh=!0,wh=y.ytLoggingTransportGELQueue_||new Map;A("ytLoggingTransportGELQueue_",wh,void 0);var xh=y.ytLoggingTransportTokensToCttTargetIds_||{};A("ytLoggingTransportTokensToCttTargetIds_",xh,void 0);
function yh(a,b){if("log_event"===a.endpoint){var c="";a.ia?c="visitorOnlyApprovedKey":a.cttAuthInfo&&(xh[a.cttAuthInfo.token]=zh(a.cttAuthInfo),c=a.cttAuthInfo.token);var d=wh.get(c)||[];wh.set(c,d);d.push(a.payload);b&&(rh=new b);a=Rf("tvhtml5_logging_max_batch")||Rf("web_logging_max_batch")||100;b=P();d.length>=a?Ah({writeThenSend:!0},O("flush_only_full_queue")?c:void 0):10<=b-uh&&(Bh(),uh=b)}}
function Ch(a,b){if("log_event"===a.endpoint){var c="";a.ia?c="visitorOnlyApprovedKey":a.cttAuthInfo&&(xh[a.cttAuthInfo.token]=zh(a.cttAuthInfo),c=a.cttAuthInfo.token);var d=new Map;d.set(c,[a.payload]);b&&(rh=new b);return new Ve(function(e){rh&&rh.isReady()?Dh(d,e,{bypassNetworkless:!0}):e()})}}
function Ah(a,b){a=void 0===a?{}:a;new Ve(function(c){dg(sh);dg(th);th=0;if(rh&&rh.isReady())if(void 0!==b){var d=new Map,e=wh.get(b)||[];d.set(b,e);Dh(d,c,a);wh.delete(b)}else Dh(wh,c,a),wh.clear();else Bh(),c()})}
function Bh(){O("web_gel_timeout_cap")&&!th&&(th=cg(function(){Ah({writeThenSend:!0})},6E4));
dg(sh);var a=F("LOGGING_BATCH_TIMEOUT",Rf("web_gel_debounce_ms",1E4));O("shorten_initial_gel_batch_timeout")&&vh&&(a=nh);sh=cg(function(){Ah({writeThenSend:!0})},a)}
function Dh(a,b,c){var d=rh;c=void 0===c?{}:c;var e=Math.round(P()),f=a.size;a=u(a);for(var g=a.next();!g.done;g=a.next()){var h=u(g.value);g=h.next().value;var k=h=h.next().value;h=lb({context:Eh(d.config_||Fh())});h.events=k;(k=xh[g])&&Gh(h,g,k);delete xh[g];g="visitorOnlyApprovedKey"===g;Hh(h,e,g);O("send_beacon_before_gel")&&window.navigator&&window.navigator.sendBeacon&&!c.writeThenSend&&bh("/generate_204");Ih(d,"log_event",h,{retry:!0,onSuccess:function(){f--;f||b();qh=Math.round(P()-e)},
onError:function(){f--;f||b()},
La:c,ia:g});vh=!1}}
function Hh(a,b,c){a.requestTimeMs=String(b);O("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);!c&&(b=F("EVENT_ID",void 0))&&((c=F("BATCH_CLIENT_COUNTER",void 0)||0)||(c=Math.floor(Math.random()*oh/2)),c++,c>oh&&(c=1),N("BATCH_CLIENT_COUNTER",c),b={serializedEventId:b,clientCounter:String(c)},a.serializedClientEventId=b,ph&&qh&&O("log_gel_rtt_web")&&(a.previousBatchInfo={serializedClientEventId:ph,roundtripMs:String(qh)}),ph=b,qh=0)}
function Gh(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
function zh(a){var b={};a.videoId?b.videoId=a.videoId:a.playlistId&&(b.playlistId=a.playlistId);return b}
;var Jh=y.ytLoggingGelSequenceIdObj_||{};A("ytLoggingGelSequenceIdObj_",Jh,void 0);
function Kh(a,b,c,d){d=void 0===d?{}:d;var e={},f=Math.round(d.timestamp||P());e.eventTimeMs=f<Number.MAX_SAFE_INTEGER?f:0;e[a]=b;a=pg();e.context={lastActivityMs:String(d.timestamp||!isFinite(a)?-1:a)};O("log_sequence_info_on_gel_web")&&d.U&&(a=e.context,b=d.U,Jh[b]=b in Jh?Jh[b]+1:0,a.sequence={index:Jh[b],groupKey:b},d.Va&&delete Jh[d.U]);(d.Ul?Ch:yh)({endpoint:"log_event",payload:e,cttAuthInfo:d.cttAuthInfo,ia:d.ia},c)}
;function Lh(){if(!y.matchMedia)return"WEB_DISPLAY_MODE_UNKNOWN";try{return y.matchMedia("(display-mode: standalone)").matches?"WEB_DISPLAY_MODE_STANDALONE":y.matchMedia("(display-mode: minimal-ui)").matches?"WEB_DISPLAY_MODE_MINIMAL_UI":y.matchMedia("(display-mode: fullscreen)").matches?"WEB_DISPLAY_MODE_FULLSCREEN":y.matchMedia("(display-mode: browser)").matches?"WEB_DISPLAY_MODE_BROWSER":"WEB_DISPLAY_MODE_UNKNOWN"}catch(a){return"WEB_DISPLAY_MODE_UNKNOWN"}}
;function Mh(a,b,c,d,e){od.set(""+a,b,{ya:c,path:"/",domain:void 0===d?"youtube.com":d,secure:void 0===e?!1:e})}
;var Nh=B("ytglobal.prefsUserPrefsPrefs_")||{};A("ytglobal.prefsUserPrefsPrefs_",Nh,void 0);function Oh(){this.h=F("ALT_PREF_COOKIE_NAME","PREF");this.i=F("ALT_PREF_COOKIE_DOMAIN","youtube.com");var a=od.get(""+this.h,void 0);if(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(Nh[d]=c.toString())}}}
Oh.prototype.get=function(a,b){Ph(a);Qh(a);a=void 0!==Nh[a]?Nh[a].toString():null;return null!=a?a:b?b:""};
Oh.prototype.set=function(a,b){Ph(a);Qh(a);if(null==b)throw Error("ExpectedNotNull");Nh[a]=b.toString()};
Oh.prototype.remove=function(a){Ph(a);Qh(a);delete Nh[a]};
Oh.prototype.clear=function(){for(var a in Nh)delete Nh[a]};
function Qh(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function Ph(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function Rh(a){a=void 0!==Nh[a]?Nh[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
Fa(Oh);var Sh={bluetooth:"CONN_DISCO",cellular:"CONN_CELLULAR_UNKNOWN",ethernet:"CONN_WIFI",none:"CONN_NONE",wifi:"CONN_WIFI",wimax:"CONN_CELLULAR_4G",other:"CONN_UNKNOWN",unknown:"CONN_UNKNOWN","slow-2g":"CONN_CELLULAR_2G","2g":"CONN_CELLULAR_2G","3g":"CONN_CELLULAR_3G","4g":"CONN_CELLULAR_4G"},Th={"slow-2g":"EFFECTIVE_CONNECTION_TYPE_SLOW_2G","2g":"EFFECTIVE_CONNECTION_TYPE_2G","3g":"EFFECTIVE_CONNECTION_TYPE_3G","4g":"EFFECTIVE_CONNECTION_TYPE_4G"};
function Uh(){var a=y.navigator;return a?a.connection:void 0}
;function Vh(){return"INNERTUBE_API_KEY"in If&&"INNERTUBE_API_VERSION"in If}
function Fh(){return{innertubeApiKey:F("INNERTUBE_API_KEY",void 0),innertubeApiVersion:F("INNERTUBE_API_VERSION",void 0),Xa:F("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),Ya:F("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:F("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0),ab:F("INNERTUBE_CONTEXT_HL",void 0),Za:F("INNERTUBE_CONTEXT_GL",void 0),bb:F("INNERTUBE_HOST_OVERRIDE",void 0)||"",eb:!!F("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),cb:!!F("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",
!1),appInstallData:F("SERIALIZED_CLIENT_CONFIG_DATA",void 0)}}
function Eh(a){var b={client:{hl:a.ab,gl:a.Za,clientName:a.Ya,clientVersion:a.innertubeContextClientVersion,configInfo:a.Xa}};navigator.userAgent&&(b.client.userAgent=String(navigator.userAgent));var c=y.devicePixelRatio;c&&1!=c&&(b.client.screenDensityFloat=String(c));c=F("EXPERIMENTS_TOKEN","");""!==c&&(b.client.experimentsToken=c);c=[];var d=F("EXPERIMENTS_FORCED_FLAGS",{});for(e in d)c.push({key:e,value:String(d[e])});var e=F("EXPERIMENT_FLAGS",{});for(var f in e)f.startsWith("force_")&&void 0===
d[f]&&c.push({key:f,value:String(e[f])});0<c.length&&(b.request={internalExperimentFlags:c});f=b.client.clientName;if("WEB"===f||"MWEB"===f||1===f||2===f){if(!O("web_include_display_mode_killswitch")){var g;b.client.mainAppWebInfo=null!=(g=b.client.mainAppWebInfo)?g:{};b.client.mainAppWebInfo.webDisplayMode=Lh()}}else if(g=b.client.clientName,("WEB_REMIX"===g||76===g)&&!O("music_web_display_mode_killswitch")){var h;b.client.Ja=null!=(h=b.client.Ja)?h:{};b.client.Ja.webDisplayMode=Lh()}a.appInstallData&&
(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.appInstallData=a.appInstallData);F("DELEGATED_SESSION_ID")&&!O("pageid_as_header_web")&&(b.user={onBehalfOfUser:F("DELEGATED_SESSION_ID")});a:{if(h=Uh()){a=Sh[h.type||"unknown"]||"CONN_UNKNOWN";h=Sh[h.effectiveType||"unknown"]||"CONN_UNKNOWN";"CONN_CELLULAR_UNKNOWN"===a&&"CONN_UNKNOWN"!==h&&(a=h);if("CONN_UNKNOWN"!==a)break a;if("CONN_UNKNOWN"!==h){a=h;break a}}a=void 0}a&&(b.client.connectionType=a);O("web_log_effective_connection_type")&&
(a=Uh(),a=null!==a&&void 0!==a&&a.effectiveType?Th.hasOwnProperty(a.effectiveType)?Th[a.effectiveType]:"EFFECTIVE_CONNECTION_TYPE_UNKNOWN":void 0,a&&(b.client.effectiveConnectionType=a));a=Object;h=a.assign;g=b.client;f={};e=u(Object.entries(zg(F("DEVICE",""))));for(c=e.next();!c.done;c=e.next())d=u(c.value),c=d.next().value,d=d.next().value,"cbrand"===c?f.deviceMake=d:"cmodel"===c?f.deviceModel=d:"cbr"===c?f.browserName=d:"cbrver"===c?f.browserVersion=d:"cos"===c?f.osName=d:"cosver"===c?f.osVersion=
d:"cplatform"===c&&(f.platform=d);b.client=h.call(a,g,f);return b}
function Wh(a,b,c){c=void 0===c?{}:c;var d={"X-Goog-Visitor-Id":c.visitorData||F("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;(b=c.Ll||F("AUTHORIZATION"))||(a?b="Bearer "+B("gapi.auth.getToken")().Kl:b=sd([]));b&&(d.Authorization=b,d["X-Goog-AuthUser"]=F("SESSION_INDEX",0),O("pageid_as_header_web")&&(d["X-Goog-PageId"]=F("DELEGATED_SESSION_ID")));return d}
;function Xh(a){a=Object.assign({},a);delete a.Authorization;var b=sd();if(b){var c=new Md;c.update(F("INNERTUBE_API_KEY",void 0));c.update(b);a.hash=Ec(c.digest())}return a}
;function Yh(a){var b=new xf;(b=b.isAvailable()?a?new Df(b,a):b:null)||(a=new yf(a||"UserDataSharedStore"),b=a.isAvailable()?a:null);this.h=(a=b)?new tf(a):null;this.i=document.domain||window.location.hostname}
Yh.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.h)try{this.h.set(a,b,Date.now()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(Oe(b))}catch(f){return}else e=escape(b);Mh(a,e,c,this.i)};
Yh.prototype.get=function(a,b){var c=void 0,d=!this.h;if(!d)try{c=this.h.get(a)}catch(e){d=!0}if(d&&(c=od.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
Yh.prototype.remove=function(a){this.h&&this.h.remove(a);var b=this.i;od.remove(""+a,"/",void 0===b?"youtube.com":b)};var Zh;function $h(){Zh||(Zh=new Yh("yt.innertube"));return Zh}
function ai(a,b,c,d){if(d)return null;d=$h().get("nextId",!0)||1;var e=$h().get("requests",!0)||{};e[d]={method:a,request:b,authState:Xh(c),requestTime:Math.round(P())};$h().set("nextId",d+1,86400,!0);$h().set("requests",e,86400,!0);return d}
function bi(a){var b=$h().get("requests",!0)||{};delete b[a];$h().set("requests",b,86400,!0)}
function ci(a){var b=$h().get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(P())-d.requestTime)){var e=d.authState,f=Xh(Wh(!1));jb(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(P())),Ih(a,d.method,e,{}));delete b[c]}}$h().set("requests",b,86400,!0)}}
;function di(a,b){this.version=a;this.args=b}
;function ei(a,b){this.topic=a;this.h=b}
ei.prototype.toString=function(){return this.topic};var fi=B("ytPubsub2Pubsub2Instance")||new M;M.prototype.subscribe=M.prototype.subscribe;M.prototype.unsubscribeByKey=M.prototype.ca;M.prototype.publish=M.prototype.W;M.prototype.clear=M.prototype.clear;A("ytPubsub2Pubsub2Instance",fi,void 0);var gi=B("ytPubsub2Pubsub2SubscribedKeys")||{};A("ytPubsub2Pubsub2SubscribedKeys",gi,void 0);var hi=B("ytPubsub2Pubsub2TopicToKeys")||{};A("ytPubsub2Pubsub2TopicToKeys",hi,void 0);var ii=B("ytPubsub2Pubsub2IsAsync")||{};A("ytPubsub2Pubsub2IsAsync",ii,void 0);
A("ytPubsub2Pubsub2SkipSubKey",null,void 0);function ji(a,b){var c=ki();c&&c.publish.call(c,a.toString(),a,b)}
function li(a){var b=mi,c=ki();if(!c)return 0;var d=c.subscribe(b.toString(),function(e,f){var g=B("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=function(){if(gi[d])try{if(f&&b instanceof ei&&b!=e)try{var h=b.h,k=f;if(!k.args||!k.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!h.V){var l=new h;h.V=l.version}var n=h.V}catch(q){}if(!n||k.version!=n)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{f=Reflect.construct(h,
bb(k.args))}catch(q){throw q.message="yt.pubsub2.Data.deserialize(): "+q.message,q;}}catch(q){throw q.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+q.message,q;}a.call(window,f)}catch(q){Mf(q)}},ii[b.toString()]?B("yt.scheduler.instance")?ig(g):cg(g,0):g())});
gi[d]=!0;hi[b.toString()]||(hi[b.toString()]=[]);hi[b.toString()].push(d);return d}
function ni(){var a=oi,b=li(function(c){a.apply(void 0,arguments);pi(b)});
return b}
function pi(a){var b=ki();b&&("number"===typeof a&&(a=[a]),D(a,function(c){b.unsubscribeByKey(c);delete gi[c]}))}
function ki(){return B("ytPubsub2Pubsub2Instance")}
;var qi=function(){var a;return function(){a||(a=new Yh("ytidb"));return a}}();
function ri(){var a;return null===(a=qi())||void 0===a?void 0:a.get("LAST_RESULT_ENTRY_KEY",!0)}
function si(a){this.h=void 0===a?!1:a;(a=ri())||(a={hasSucceededOnce:this.h});this.i=a;var b,c;null!==(b=qi())&&void 0!==b&&b.h&&(b={hasSucceededOnce:this.i.hasSucceededOnce||this.h},null===(c=qi())||void 0===c?void 0:c.set("LAST_RESULT_ENTRY_KEY",b,2592E3,!0))}
si.prototype.isSupported=function(){return this.h};var ti=[],ui=!1;function vi(a){ui||(ti.push({type:"ERROR",payload:a}),10<ti.length&&ti.shift())}
function wi(a,b){ui||(ti.push({type:"EVENT",eventType:a,payload:b}),10<ti.length&&ti.shift())}
;function xi(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];d=Error.call(this,a);this.message=d.message;"stack"in d&&(this.stack=d.stack);this.args=[].concat(fa(c))}
v(xi,Error);function yi(){try{return zi(),!0}catch(a){return!1}}
function zi(){if(void 0!==F("DATASYNC_ID",void 0))return F("DATASYNC_ID",void 0);throw new xi("Datasync ID not set","unknown");}
;function Ai(a){if(0<=a.indexOf(":"))throw Error("Database name cannot contain ':'");}
function Bi(a){return a.substr(0,a.indexOf(":"))||a}
;var Ci={},Di=(Ci.AUTH_INVALID="No user identifier specified.",Ci.EXPLICIT_ABORT="Transaction was explicitly aborted.",Ci.IDB_NOT_SUPPORTED="IndexedDB is not supported.",Ci.MISSING_INDEX="Index not created.",Ci.MISSING_OBJECT_STORE="Object store not created.",Ci.DB_DELETED_BY_MISSING_OBJECT_STORE="Database is deleted because an expected object store was not created.",Ci.UNKNOWN_ABORT="Transaction was aborted for unknown reasons.",Ci.QUOTA_EXCEEDED="The current transaction exceeded its quota limitations.",
Ci.QUOTA_MAYBE_EXCEEDED="The current transaction may have failed because of exceeding quota limitations.",Ci.EXECUTE_TRANSACTION_ON_CLOSED_DB="Can't start a transaction on a closed database",Ci.INCOMPATIBLE_DB_VERSION="The binary is incompatible with the database version",Ci),Ei={},Fi=(Ei.AUTH_INVALID="ERROR",Ei.EXECUTE_TRANSACTION_ON_CLOSED_DB="WARNING",Ei.EXPLICIT_ABORT="IGNORED",Ei.IDB_NOT_SUPPORTED="ERROR",Ei.MISSING_INDEX="WARNING",Ei.MISSING_OBJECT_STORE="ERROR",Ei.DB_DELETED_BY_MISSING_OBJECT_STORE=
"WARNING",Ei.QUOTA_EXCEEDED="WARNING",Ei.QUOTA_MAYBE_EXCEEDED="WARNING",Ei.UNKNOWN_ABORT="WARNING",Ei.INCOMPATIBLE_DB_VERSION="WARNING",Ei),Gi={},Hi=(Gi.AUTH_INVALID=!1,Gi.EXECUTE_TRANSACTION_ON_CLOSED_DB=!1,Gi.EXPLICIT_ABORT=!1,Gi.IDB_NOT_SUPPORTED=!1,Gi.MISSING_INDEX=!1,Gi.MISSING_OBJECT_STORE=!1,Gi.DB_DELETED_BY_MISSING_OBJECT_STORE=!1,Gi.QUOTA_EXCEEDED=!1,Gi.QUOTA_MAYBE_EXCEEDED=!0,Gi.UNKNOWN_ABORT=!0,Gi.INCOMPATIBLE_DB_VERSION=!1,Gi);
function Q(a,b,c,d,e){b=void 0===b?{}:b;c=void 0===c?Di[a]:c;d=void 0===d?Fi[a]:d;e=void 0===e?Hi[a]:e;xi.call(this,c,Object.assign({name:"YtIdbKnownError",isSw:void 0===self.document,isIframe:self!==self.top,type:a},b));this.type=a;this.message=c;this.level=d;this.h=e;Object.setPrototypeOf(this,Q.prototype)}
v(Q,xi);function Ii(a){Q.call(this,"MISSING_OBJECT_STORE",{gb:a},Di.MISSING_OBJECT_STORE);Object.setPrototypeOf(this,Ii.prototype)}
v(Ii,Q);function Ji(a,b){var c=Error.call(this);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.index=a;this.objectStore=b;Object.setPrototypeOf(this,Ji.prototype)}
v(Ji,Error);var Ki=["The database connection is closing","Can't start a transaction on a closed database","A mutation operation was attempted on a database that did not allow mutations"];
function Li(a,b,c,d){b=Bi(b);var e=a instanceof Error?a:Error("Unexpected error: "+a);if(e instanceof Q)return e;if("QuotaExceededError"===e.name)return new Q("QUOTA_EXCEEDED",{objectStoreNames:c,dbName:b});if(Bc&&"UnknownError"===e.name)return new Q("QUOTA_MAYBE_EXCEEDED",{objectStoreNames:c,dbName:b});if(e instanceof Ji)return new Q("MISSING_INDEX",{dbName:b,dbVersion:d,objectStore:e.objectStore,index:e.index});if("InvalidStateError"===e.name&&Ki.some(function(f){return e.message.includes(f)}))return new Q("EXECUTE_TRANSACTION_ON_CLOSED_DB",
{objectStoreNames:c,
dbName:b});if("AbortError"===e.name)return new Q("UNKNOWN_ABORT",{objectStoreNames:c,dbName:b},e.message);e.args=[{name:"IdbError",Ql:e.name,dbName:b,objectStoreNames:c}];e.level="WARNING";return e}
function Mi(a,b,c){return new Q("IDB_NOT_SUPPORTED",{context:{caller:a,publicName:b,version:c}})}
;function Ni(a){if(!a)throw Error();throw a;}
function Oi(a){return a}
function Pi(a){this.h=a}
function S(a){function b(e){if("PENDING"===d.state.status){d.state={status:"REJECTED",reason:e};e=u(d.onRejected);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
function c(e){if("PENDING"===d.state.status){d.state={status:"FULFILLED",value:e};e=u(d.h);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
var d=this;this.state={status:"PENDING"};this.h=[];this.onRejected=[];a=a.h;try{a(c,b)}catch(e){b(e)}}
S.all=function(a){return new S(new Pi(function(b,c){var d=[],e=a.length;0===e&&b(d);for(var f={Y:0};f.Y<a.length;f={Y:f.Y},++f.Y)Qi(S.resolve(a[f.Y]).then(function(g){return function(h){d[g.Y]=h;e--;0===e&&b(d)}}(f)),function(g){c(g)})}))};
S.resolve=function(a){return new S(new Pi(function(b,c){a instanceof S?a.then(b,c):b(a)}))};
S.reject=function(a){return new S(new Pi(function(b,c){c(a)}))};
S.prototype.then=function(a,b){var c=this,d=null!==a&&void 0!==a?a:Oi,e=null!==b&&void 0!==b?b:Ni;return new S(new Pi(function(f,g){"PENDING"===c.state.status?(c.h.push(function(){Ri(c,c,d,f,g)}),c.onRejected.push(function(){Si(c,c,e,f,g)})):"FULFILLED"===c.state.status?Ri(c,c,d,f,g):"REJECTED"===c.state.status&&Si(c,c,e,f,g)}))};
function Qi(a,b){a.then(void 0,b)}
function Ri(a,b,c,d,e){try{if("FULFILLED"!==a.state.status)throw Error("calling handleResolve before the promise is fulfilled.");var f=c(a.state.value);f instanceof S?Ti(a,b,f,d,e):d(f)}catch(g){e(g)}}
function Si(a,b,c,d,e){try{if("REJECTED"!==a.state.status)throw Error("calling handleReject before the promise is rejected.");var f=c(a.state.reason);f instanceof S?Ti(a,b,f,d,e):d(f)}catch(g){e(g)}}
function Ti(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(function(f){f instanceof S?Ti(a,b,f,d,e):d(f)},function(f){e(f)})}
;function Ui(a,b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){try{a.removeEventListener("success",e),a.removeEventListener("error",d)}catch(g){}}
a.addEventListener("success",e);a.addEventListener("error",d)}
function Vi(a){return new Promise(function(b,c){Ui(a,b,c)})}
function Wi(a){return new S(new Pi(function(b,c){Ui(a,b,c)}))}
;function Xi(a,b){return new S(new Pi(function(c,d){function e(){var f=a?b(a):null;f?f.then(function(g){a=g;e()},d):c()}
e()}))}
;function Yi(a,b){this.h=a;this.options=b;this.transactionCount=0;this.j=Math.round(P());this.i=!1}
m=Yi.prototype;m.add=function(a,b,c){return Zi(this,[a],{mode:"readwrite",H:!0},function(d){return d.objectStore(a).add(b,c)})};
m.clear=function(a){return Zi(this,[a],{mode:"readwrite",H:!0},function(b){return b.objectStore(a).clear()})};
m.close=function(){var a;this.h.close();(null===(a=this.options)||void 0===a?0:a.closed)&&this.options.closed()};
m.count=function(a,b){return Zi(this,[a],{mode:"readonly",H:!0},function(c){return c.objectStore(a).count(b)})};
function $i(a,b,c){a=a.h.createObjectStore(b,c);return new aj(a)}
m.delete=function(a,b){return Zi(this,[a],{mode:"readwrite",H:!0},function(c){return c.objectStore(a).delete(b)})};
m.get=function(a,b){return Zi(this,[a],{mode:"readonly",H:!0},function(c){return c.objectStore(a).get(b)})};
function bj(a,b){return Zi(a,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(c){c=c.objectStore("LogsRequestsStore");return Wi(c.h.put(b,void 0))})}
m.objectStoreNames=function(){return Array.from(this.h.objectStoreNames)};
function Zi(a,b,c,d){return H(a,function f(){var g=this,h,k,l,n,q,r,p,z,I,E,R,V;return x(f,function(J){switch(J.h){case 1:var U={mode:"readonly",H:!1,tag:"IDB_TRANSACTION_TAG_UNKNOWN"};"string"===typeof c?U.mode=c:Object.assign(U,c);h=U;g.transactionCount++;k=h.H?3:1;l=0;case 2:if(n){J.B(3);break}l++;q=Math.round(P());ra(J,4);r=g.h.transaction(b,h.mode);U=new cj(r);U=dj(U,d);return w(J,U,6);case 6:return p=J.i,z=Math.round(P()),ej(g,q,z,l,void 0,b.join(),h),J.return(p);case 4:I=sa(J);E=Math.round(P());
R=Li(I,g.h.name,b.join(),g.h.version);if((V=R instanceof Q&&!R.h)||l>=k)ej(g,q,E,l,R,b.join(),h),n=R;J.B(2);break;case 3:return J.return(Promise.reject(n))}})})}
function ej(a,b,c,d,e,f,g){b=c-b;e?(e instanceof Q&&("QUOTA_EXCEEDED"===e.type||"QUOTA_MAYBE_EXCEEDED"===e.type)&&wi("QUOTA_EXCEEDED",{dbName:Bi(a.h.name),objectStoreNames:f,transactionCount:a.transactionCount,transactionMode:g.mode}),e instanceof Q&&"UNKNOWN_ABORT"===e.type&&(c-=a.j,0>c&&c>=Math.pow(2,31)&&(c=0),wi("TRANSACTION_UNEXPECTEDLY_ABORTED",{objectStoreNames:f,transactionDuration:b,transactionCount:a.transactionCount,dbDuration:c}),a.i=!0),fj(a,!1,d,f,b,g.tag),vi(e)):fj(a,!0,d,f,b,g.tag)}
function fj(a,b,c,d,e,f){wi("TRANSACTION_ENDED",{objectStoreNames:d,connectionHasUnknownAbortedTransaction:a.i,duration:e,isSuccessful:b,tryCount:c,tag:void 0===f?"IDB_TRANSACTION_TAG_UNKNOWN":f})}
m.getName=function(){return this.h.name};
function aj(a){this.h=a}
m=aj.prototype;m.add=function(a,b){return Wi(this.h.add(a,b))};
m.autoIncrement=function(){return this.h.autoIncrement};
m.clear=function(){return Wi(this.h.clear()).then(function(){})};
m.count=function(a){return Wi(this.h.count(a))};
function gj(a,b){return hj(a,{query:b},function(c){return c.delete().then(function(){return c.continue()})}).then(function(){})}
m.delete=function(a){return a instanceof IDBKeyRange?gj(this,a):Wi(this.h.delete(a))};
m.get=function(a){return Wi(this.h.get(a))};
m.index=function(a){try{return new ij(this.h.index(a))}catch(b){if(b instanceof Error&&"NotFoundError"===b.name)throw new Ji(a,this.h.name);throw b;}};
m.getName=function(){return this.h.name};
m.keyPath=function(){return this.h.keyPath};
function hj(a,b,c){a=a.h.openCursor(b.query,b.direction);return jj(a).then(function(d){return Xi(d,c)})}
function cj(a){var b=this;this.h=a;this.j=new Map;this.i=!1;this.done=new Promise(function(c,d){b.h.addEventListener("complete",function(){c()});
b.h.addEventListener("error",function(e){e.currentTarget===e.target&&d(b.h.error)});
b.h.addEventListener("abort",function(){var e=b.h.error;if(e)d(e);else if(!b.i){e=Q;for(var f=b.h.objectStoreNames,g=[],h=0;h<f.length;h++){var k=f.item(h);if(null===k)throw Error("Invariant: item in DOMStringList is null");g.push(k)}e=new e("UNKNOWN_ABORT",{objectStoreNames:g.join(),dbName:b.h.db.name,mode:b.h.mode});d(e)}})})}
function dj(a,b){var c=new Promise(function(d,e){try{Qi(b(a).then(function(f){d(f)}),e)}catch(f){e(f),a.abort()}});
return Promise.all([c,a.done]).then(function(d){return u(d).next().value})}
cj.prototype.abort=function(){this.h.abort();this.i=!0;throw new Q("EXPLICIT_ABORT");};
cj.prototype.objectStore=function(a){a=this.h.objectStore(a);var b=this.j.get(a);b||(b=new aj(a),this.j.set(a,b));return b};
function ij(a){this.h=a}
m=ij.prototype;m.count=function(a){return Wi(this.h.count(a))};
m.delete=function(a){return kj(this,{query:a},function(b){return b.delete().then(function(){return b.continue()})})};
m.get=function(a){return Wi(this.h.get(a))};
m.getKey=function(a){return Wi(this.h.getKey(a))};
m.keyPath=function(){return this.h.keyPath};
m.unique=function(){return this.h.unique};
function kj(a,b,c){a=a.h.openCursor(void 0===b.query?null:b.query,void 0===b.direction?"next":b.direction);return jj(a).then(function(d){return Xi(d,c)})}
function lj(a,b){this.request=a;this.cursor=b}
function jj(a){return Wi(a).then(function(b){return b?new lj(a,b):null})}
m=lj.prototype;m.advance=function(a){this.cursor.advance(a);return jj(this.request)};
m.continue=function(a){this.cursor.continue(a);return jj(this.request)};
m.delete=function(){return Wi(this.cursor.delete()).then(function(){})};
m.getKey=function(){return this.cursor.key};
m.getValue=function(){return this.cursor.value};
m.update=function(a){return Wi(this.cursor.update(a))};function mj(a,b,c){return new Promise(function(d,e){function f(){r||(r=new Yi(g.result,{closed:q}));return r}
var g=void 0!==b?self.indexedDB.open(a,b):self.indexedDB.open(a);var h=c.blocked,k=c.blocking,l=c.vb,n=c.upgrade,q=c.closed,r;g.addEventListener("upgradeneeded",function(p){try{if(null===p.newVersion)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");if(null===g.transaction)throw Error("Invariant: transaction on IDbOpenDbRequest is null");p.dataLoss&&"none"!==p.dataLoss&&wi("IDB_DATA_CORRUPTED",{reason:p.dataLossMessage||"unknown reason",dbName:Bi(a)});var z=f(),I=new cj(g.transaction);
n&&n(z,function(E){return p.oldVersion<E&&p.newVersion>=E},I);
I.done.catch(function(E){e(E)})}catch(E){e(E)}});
g.addEventListener("success",function(){var p=g.result;k&&p.addEventListener("versionchange",function(){k(f())});
p.addEventListener("close",function(){wi("IDB_UNEXPECTEDLY_CLOSED",{dbName:Bi(a),dbVersion:p.version});l&&l()});
d(f())});
g.addEventListener("error",function(){e(g.error)});
h&&g.addEventListener("blocked",function(){h()})})}
function nj(a,b,c){c=void 0===c?{}:c;return mj(a,b,c)}
function oj(a,b){b=void 0===b?{}:b;return H(this,function d(){var e,f,g;return x(d,function(h){e=self.indexedDB.deleteDatabase(a);f=b;(g=f.blocked)&&e.addEventListener("blocked",function(){g()});
return w(h,Vi(e),0)})})}
;function pj(a,b){this.name=a;this.options=b;this.l=!0;this.j=!1}
pj.prototype.i=function(a,b,c){c=void 0===c?{}:c;return nj(a,b,c)};
pj.prototype.delete=function(a){a=void 0===a?{}:a;return oj(this.name,a)};
function qj(a,b){return new Q("INCOMPATIBLE_DB_VERSION",{dbName:a.name,oldVersion:a.options.version,newVersion:b})}
pj.prototype.open=function(){function a(){return H(c,function g(){var h=this,k,l,n,q,r;return x(g,function(p){switch(p.h){case 1:return ra(p,2),w(p,h.i(h.name,h.options.version,e),4);case 4:k=p.i;a:{var z=h.options;for(var I=u(Object.keys(z.ka)),E=I.next();!E.done;E=I.next()){E=E.value;var R=z.ka[E],V=void 0===R.mb?Number.MAX_VALUE:R.mb;if(k.h.version>=R.qa&&!(k.h.version>=V)&&!k.h.objectStoreNames.contains(E)){z=E;break a}}z=void 0}l=z;if(void 0===l){p.B(5);break}if(h.j){p.B(6);break}h.j=!0;return w(p,
h.delete(),7);case 7:return vi(new Q("DB_DELETED_BY_MISSING_OBJECT_STORE",{dbName:h.name,gb:l})),p.return(a());case 6:throw new Ii(l);case 5:return p.return(k);case 2:n=sa(p);if(n instanceof DOMException?"VersionError"!==n.name:"DOMError"in self&&n instanceof DOMError?"VersionError"!==n.name:!(n instanceof Object&&"message"in n)||"An attempt was made to open a database using a lower version than the existing version."!==n.message){p.B(8);break}return w(p,h.i(h.name,void 0,Object.assign(Object.assign({},
e),{upgrade:void 0})),9);case 9:q=p.i;r=q.h.version;if(void 0!==h.options.version&&r>h.options.version+1)throw q.close(),h.l=!1,qj(h,r);return p.return(q);case 8:throw b(),n;}})})}
function b(){c.h===d&&(c.h=void 0)}
var c=this;if(!this.l)throw qj(this);if(this.h)return this.h;var d,e={blocking:function(f){f.close()},
closed:b,vb:b,upgrade:this.options.upgrade};return this.h=d=a()};var rj=new pj("YtIdbMeta",{ka:{databases:{qa:1}},upgrade:function(a,b){b(1)&&$i(a,"databases",{keyPath:"actualName"})}});
function sj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,rj.open(),2);d=e.i;return e.return(Zi(d,["databases"],{H:!0,mode:"readwrite"},function(f){var g=f.objectStore("databases");return g.get(a.actualName).then(function(h){if(h?a.actualName!==h.actualName||a.publicName!==h.publicName||a.userIdentifier!==h.userIdentifier:1)return Wi(g.h.put(a,void 0)).then(function(){})})}))})})}
function tj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return a?w(e,rj.open(),2):e.return();d=e.i;return e.return(d.delete("databases",a))})})}
function uj(a){return H(this,function c(){var d,e;return x(c,function(f){return 1==f.h?(d=[],w(f,rj.open(),2)):3!=f.h?(e=f.i,w(f,Zi(e,["databases"],{H:!0,mode:"readonly"},function(g){d.length=0;return hj(g.objectStore("databases"),{},function(h){a(h.getValue())&&d.push(h.getValue());return h.continue()})}),3)):f.return(d)})})}
function vj(){return uj(function(a){return"LogsDatabaseV2"===a.publicName&&void 0!==a.userIdentifier})}
;var wj,xj=new function(){}(new function(){});
function yj(){return H(this,function b(){var c,d,e;return x(b,function(f){switch(f.h){case 1:c=ri();if(null===c||void 0===c?0:c.hasSucceededOnce)return f.return(new si(!0));var g;if(g=Vg)g=/WebKit\/([0-9]+)/.exec(Ob),g=!!(g&&600<=parseInt(g[1],10));g&&(g=/WebKit\/([0-9]+)/.exec(Ob),g=!(g&&602<=parseInt(g[1],10)));if(g||mc)return f.return(new si(!1));try{if(d=self,!(d.indexedDB&&d.IDBIndex&&d.IDBKeyRange&&d.IDBObjectStore))return f.return(new si(!1))}catch(h){return f.return(new si(!1))}if(!("IDBTransaction"in
self&&"objectStoreNames"in IDBTransaction.prototype))return f.return(new si(!1));ra(f,2);e={actualName:"yt-idb-test-do-not-use",publicName:"yt-idb-test-do-not-use",userIdentifier:void 0};return w(f,sj(e),4);case 4:return w(f,tj("yt-idb-test-do-not-use"),5);case 5:return f.return(new si(!0));case 2:return sa(f),f.return(new si(!1))}})})}
function zj(){if(void 0!==wj)return wj;ui=!0;return wj=yj().then(function(a){ui=!1;return a.isSupported()})}
function Aj(){return zj().then(function(a){return a?xj:void 0})}
;new function(){var a=this;this.promise=new Promise(function(b,c){a.resolve=b;a.reject=c})};function Bj(a){if(!yi())throw a=new Q("AUTH_INVALID",{dbName:a}),vi(a),a;var b=zi();return{actualName:a+":"+b,publicName:a,userIdentifier:b}}
function Cj(a,b,c,d){return H(this,function f(){var g,h,k,l;return x(f,function(n){switch(n.h){case 1:return w(n,Aj(),2);case 2:g=n.i;if(!g)throw h=Mi("openDbImpl",a,b),vi(h),h;Ai(a);k=c?{actualName:a,publicName:a,userIdentifier:void 0}:Bj(a);ra(n,3);return w(n,sj(k),5);case 5:return w(n,nj(k.actualName,b,d),6);case 6:return n.return(n.i);case 3:return l=sa(n),ra(n,7),w(n,tj(k.actualName),9);case 9:n.h=8;n.m=0;break;case 7:sa(n);case 8:throw l;}})})}
function Dj(a,b,c){c=void 0===c?{}:c;return Cj(a,b,!1,c)}
function Ej(a,b,c){c=void 0===c?{}:c;return Cj(a,b,!0,c)}
function Fj(a,b){b=void 0===b?{}:b;return H(this,function d(){var e,f;return x(d,function(g){if(1==g.h)return w(g,Aj(),2);if(3!=g.h){e=g.i;if(!e)return g.return();Ai(a);f=Bj(a);return w(g,oj(f.actualName,b),3)}return w(g,tj(f.actualName),0)})})}
function Gj(a,b){var c=this;a=a.map(function(d){return H(c,function f(){return x(f,function(g){return 1==g.h?w(g,oj(d.actualName,b),2):w(g,tj(d.actualName),0)})})});
return Promise.all(a).then(function(){})}
function Hj(){var a=void 0===a?{}:a;return H(this,function c(){var d,e;return x(c,function(f){if(1==f.h)return w(f,Aj(),2);if(3!=f.h){d=f.i;if(!d)return f.return();Ai("LogsDatabaseV2");return w(f,vj(),3)}e=f.i;return w(f,Gj(e,a),0)})})}
function Ij(a,b){b=void 0===b?{}:b;return H(this,function d(){var e;return x(d,function(f){if(1==f.h)return w(f,Aj(),2);if(3!=f.h){e=f.i;if(!e)return f.return();Ai(a);return w(f,oj(a,b),3)}return w(f,tj(a),0)})})}
;function Jj(a,b){pj.call(this,a,b);this.options=b;Ai(a)}
v(Jj,pj);function Kj(a,b){var c;return function(){c||(c=new Jj(a,b));return c}}
Jj.prototype.i=function(a,b,c){c=void 0===c?{}:c;return(this.options.Aa?Ej:Dj)(a,b,Object.assign({},c))};
Jj.prototype.delete=function(a){a=void 0===a?{}:a;return(this.options.Aa?Ij:Fj)(this.name,a)};
function Lj(a,b){return Kj(a,b)}
;var Mj;
function Nj(){if(Mj)return Mj();var a={};Mj=Lj("LogsDatabaseV2",{ka:(a.LogsRequestsStore={qa:2},a),Aa:!1,upgrade:function(b,c,d){c(2)&&$i(b,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0});c(3);c(5)&&(d=d.objectStore("LogsRequestsStore"),d.h.indexNames.contains("newRequest")&&d.h.deleteIndex("newRequest"),d.h.createIndex("newRequestV2",["status","interface","timestamp"],{unique:!1}));c(7)&&b.h.objectStoreNames.contains("sapisid")&&b.h.deleteObjectStore("sapisid");c(9)&&b.h.objectStoreNames.contains("SWHealthLog")&&b.h.deleteObjectStore("SWHealthLog")},
version:9});return Mj()}
;function Oj(a){return H(this,function c(){var d,e,f,g;return x(c,function(h){if(1==h.h)return d={startTime:P(),transactionType:"YT_IDB_TRANSACTION_TYPE_WRITE"},w(h,Nj().open(),2);if(3!=h.h)return e=h.i,f=Object.assign(Object.assign({},a),{options:JSON.parse(JSON.stringify(a.options)),interface:F("INNERTUBE_CONTEXT_CLIENT_NAME",0)}),w(h,bj(e,f),3);g=h.i;d.wb=P();Pj(d);return h.return(g)})})}
function Qj(a){return H(this,function c(){var d,e,f,g,h,k,l;return x(c,function(n){if(1==n.h)return d={startTime:P(),transactionType:"YT_IDB_TRANSACTION_TYPE_READ"},w(n,Nj().open(),2);if(3!=n.h)return e=n.i,f=F("INNERTUBE_CONTEXT_CLIENT_NAME",0),g=[a,f,0],h=[a,f,P()],k=IDBKeyRange.bound(g,h),l=void 0,w(n,Zi(e,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(q){return kj(q.objectStore("LogsRequestsStore").index("newRequestV2"),{query:k,direction:"prev"},function(r){r.getValue()&&(l=r.getValue(),
"NEW"===a&&(l.status="QUEUED",r.update(l)))})}),3);
d.wb=P();Pj(d);return n.return(l)})})}
function Rj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,Nj().open(),2);d=e.i;return e.return(Zi(d,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(f){var g=f.objectStore("LogsRequestsStore");return g.get(a).then(function(h){if(h)return h.status="QUEUED",Wi(g.h.put(h,void 0)).then(function(){return h})})}))})})}
function Sj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,Nj().open(),2);d=e.i;return e.return(Zi(d,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(f){var g=f.objectStore("LogsRequestsStore");return g.get(a).then(function(h){return h?(h.status="NEW",h.sendCount+=1,Wi(g.h.put(h,void 0)).then(function(){return h})):S.resolve(void 0)})}))})})}
function Tj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,Nj().open(),2);d=e.i;return e.return(d.delete("LogsRequestsStore",a))})})}
function Uj(){return H(this,function b(){var c,d;return x(b,function(e){if(1==e.h)return w(e,Nj().open(),2);c=e.i;d=P()-2592E6;return w(e,Zi(c,["LogsRequestsStore"],{mode:"readwrite",H:!0},function(f){return hj(f.objectStore("LogsRequestsStore"),{},function(g){if(g.getValue().timestamp<=d)return g.delete().then(function(){return g.continue()})})}),0)})})}
function Vj(){return H(this,function b(){return x(b,function(c){return w(c,Hj(),0)})})}
function Pj(a){O("nwl_csi_killswitch")||.01>=Math.random()&&ji("nwl_transaction_latency_payload",a)}
;var Wj={},Xj=Lj("ServiceWorkerLogsDatabase",{ka:(Wj.SWHealthLog={qa:1},Wj),Aa:!0,upgrade:function(a,b){b(1)&&$i(a,"SWHealthLog",{keyPath:"id",autoIncrement:!0}).h.createIndex("swHealthNewRequest",["interface","timestamp"],{unique:!1})},
version:1});function Yj(){return H(this,function b(){var c,d;return x(b,function(e){if(1==e.h)return O("web_clean_sw_logs_store")?w(e,Xj().open(),3):e.B(0);c=e.i;d=P()-2592E6;return w(e,Zi(c,["SWHealthLog"],{mode:"readwrite",H:!0},function(f){return hj(f.objectStore("SWHealthLog"),{},function(g){if(g.getValue().timestamp<=d)return g.delete().then(function(){return g.continue()})})}),0)})})}
function Zj(){return H(this,function b(){var c;return x(b,function(d){if(1==d.h)return w(d,Xj().open(),2);c=d.i;return w(d,c.clear("SWHealthLog"),0)})})}
;var ak;function bk(){ak||(ak=new Yh("yt.offline"));return ak}
function ck(a){if(O("offline_error_handling")){var b=bk().get("errors",!0)||{};b[a.message]={name:a.name,stack:a.stack};a.level&&(b[a.message].level=a.level);bk().set("errors",b,2592E3,!0)}}
;var dk=Rf("network_polling_interval",3E4);function T(){Je.call(this);this.C=0;this.F=this.l=!1;this.j=this.va();ek(this);fk(this)}
v(T,Je);function gk(){if(!T.h){var a=B("yt.networkStatusManager.instance")||new T;A("yt.networkStatusManager.instance",a,void 0);T.h=a}return T.h}
m=T.prototype;m.K=function(){return this.j};
m.Ka=function(a,b){a!==this.j&&((void 0===b?0:b)?this.T():this.j=a)};
m.hb=function(a){this.l=!0;if(void 0===a?0:a)this.C||hk(this)};
m.va=function(){var a=window.navigator.onLine;return void 0===a?!0:a};
m.Sa=function(){this.F=!0};
m.ba=function(a,b){return Je.prototype.ba.call(this,a,b)};
function fk(a){window.addEventListener("online",function(){return H(a,function c(){var d=this;return x(c,function(e){if(1==e.h)return w(e,d.T(),2);if(d.F&&O("offline_error_handling")){var f=bk().get("errors",!0);if(f){for(var g in f)if(f[g]){var h=new xi(g,"sent via offline_errors");h.name=f[g].name;h.stack=f[g].stack;h.level=f[g].level;Mf(h)}bk().set("errors",{},2592E3,!0)}}e.h=0})})})}
function ek(a){window.addEventListener("offline",function(){return H(a,function c(){var d=this;return x(c,function(e){return w(e,d.T(),0)})})})}
function hk(a){a.C=gg(function(){return H(a,function c(){var d=this;return x(c,function(e){if(1==e.h)return d.j?d.va()||!d.l?e.B(3):w(e,d.T(),3):w(e,d.T(),3);hk(d);e.h=0})})},dk)}
m.T=function(a){var b=this;return this.m?this.m:this.m=new Promise(function(c){return H(b,function e(){var f,g,h,k=this;return x(e,function(l){switch(l.h){case 1:return f=window.AbortController?new window.AbortController:void 0,g=null===f||void 0===f?void 0:f.signal,h=!1,ra(l,2,3),f&&(k.A=ig(function(){f.abort()},a||2E4)),w(l,fetch("/generate_204",{method:"HEAD",
signal:g}),5);case 5:h=!0;case 3:ta(l);k.m=void 0;k.A&&kg(k.A);h!==k.j&&(k.j=h,k.j&&k.l?Ke(k,"ytnetworkstatus-online"):k.l&&Ke(k,"ytnetworkstatus-offline"));c(h);ua(l);break;case 2:sa(l),h=!1,l.B(3)}})})})};
T.prototype.sendNetworkCheckRequest=T.prototype.T;T.prototype.listen=T.prototype.ba;T.prototype.enableErrorFlushing=T.prototype.Sa;T.prototype.getWindowStatus=T.prototype.va;T.prototype.monitorNetworkStatusChange=T.prototype.hb;T.prototype.networkStatusHint=T.prototype.Ka;T.prototype.isNetworkAvailable=T.prototype.K;T.getInstance=gk;function ik(a){a=void 0===a?{}:a;Je.call(this);var b=this;this.l=this.A=0;this.j=gk();var c=B("yt.networkStatusManager.instance.monitorNetworkStatusChange").bind(this.j);c&&c(a.Ta);a.fb&&(c=B("yt.networkStatusManager.instance.enableErrorFlushing").bind(this.j))&&c();if(c=B("yt.networkStatusManager.instance.listen").bind(this.j))a.ma?(this.ma=a.ma,c("ytnetworkstatus-online",function(){jk(b,"publicytnetworkstatus-online")}),c("ytnetworkstatus-offline",function(){jk(b,"publicytnetworkstatus-offline")})):
(c("ytnetworkstatus-online",function(){Ke(b,"publicytnetworkstatus-online")}),c("ytnetworkstatus-offline",function(){Ke(b,"publicytnetworkstatus-offline")}))}
v(ik,Je);ik.prototype.K=function(){var a=B("yt.networkStatusManager.instance.isNetworkAvailable").bind(this.j);return a?a():!0};
ik.prototype.Ka=function(a,b){b=void 0===b?!1:b;var c=B("yt.networkStatusManager.instance.networkStatusHint").bind(this.j);c&&c(a,b)};
ik.prototype.T=function(a){return H(this,function c(){var d=this,e;return x(c,function(f){return(e=B("yt.networkStatusManager.instance.sendNetworkCheckRequest").bind(d.j))?f.return(e(a)):f.return(!0)})})};
function jk(a,b){a.ma?a.l?(kg(a.A),a.A=ig(function(){a.m!==b&&(Ke(a,b),a.m=b,a.l=P())},a.ma-(P()-a.l))):(Ke(a,b),a.m=b,a.l=P()):Ke(a,b)}
;var kk=!1,lk,mk=0,nk=0,ok,pk=y.ytNetworklessLoggingInitializationOptions||{isNwlInitialized:kk,databaseToken:lk,potentialEsfErrorCounter:nk,isIdbSupported:!!lk};A("ytNetworklessLoggingInitializationOptions",pk,void 0);
function qk(){H(this,function b(){return x(b,function(c){switch(c.h){case 1:return w(c,Aj(),2);case 2:lk=c.i;if(!lk||!yi()&&!O("nwl_init_require_datasync_id_killswitch")){c.B(0);break}kk=!0;pk.isNwlInitialized=kk;pk.databaseToken=lk;pk.isIdbSupported=!!lk;return w(c,Ij("LogsDatabaseV2"),4);case 4:if(!(.1>=Math.random())){c.B(5);break}return w(c,Uj(),6);case 6:return w(c,Yj(),5);case 5:rk();sk().K()&&tk();sk().ba("publicytnetworkstatus-online",tk);sk().ba("publicytnetworkstatus-offline",uk);if(!O("networkless_immediately_drop_sw_health_store")){c.B(8);
break}return w(c,vk(),8);case 8:if(O("networkless_immediately_drop_all_requests"))return w(c,Vj(),0);c.B(0)}})})}
function wk(a,b){function c(d){var e=sk().K();if(!xk()||!d||e&&O("vss_networkless_bypass_write"))yk(a,b);else{var f={url:a,options:b,timestamp:P(),status:"NEW",sendCount:0};Oj(f).then(function(g){f.id=g;sk().K()&&zk(f)}).catch(function(g){zk(f);
sk().K()?Mf(g):ck(g)})}}
b=void 0===b?{}:b;O("skip_is_supported_killswitch")?Aj().then(function(d){c(d)}):c(Ak())}
function Bk(a,b){function c(d){if(xk()&&d){var e={url:a,options:b,timestamp:P(),status:"NEW",sendCount:0},f=!1,g=b.onSuccess?b.onSuccess:function(){};
e.options.onSuccess=function(h,k){void 0!==e.id?Tj(e.id):f=!0;g(h,k)};
yk(e.url,e.options);Oj(e).then(function(h){e.id=h;f&&Tj(e.id)}).catch(function(h){sk().K()?Mf(h):ck(h)})}else yk(a,b)}
b=void 0===b?{}:b;O("skip_is_supported_killswitch")?Aj().then(function(d){c(d)}):c(Ak())}
function tk(){var a=this;if(!Ak())throw Mi("throttleSend");mk||(mk=ig(function(){return H(a,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,Qj("NEW"),2);if(3!=e.h)return d=e.i,d?w(e,zk(d),3):(uk(),e.return());mk&&(mk=0,tk());e.h=0})})},100))}
function uk(){kg(mk);mk=0}
function zk(a){return H(this,function c(){var d,e,f;return x(c,function(g){switch(g.h){case 1:d=Ak();if(!d)throw e=Mi("immediateSend"),e;if(void 0===a.id){g.B(2);break}return w(g,Rj(a.id),3);case 3:(f=g.i)?a=f:Nf(Error("The request cannot be found in the database."));case 2:if(Ck(a,2592E6)){g.B(4);break}Nf(Error("Networkless Logging: Stored logs request expired age limit"));if(void 0===a.id){g.B(5);break}return w(g,Tj(a.id),5);case 5:return g.return();case 4:a.skipRetry||(a=Dk(a));var h=a,k,l;if(null===
(l=null===(k=null===h||void 0===h?void 0:h.options)||void 0===k?void 0:k.postParams)||void 0===l?0:l.requestTimeMs)h.options.postParams.requestTimeMs=Math.round(P());a=h;if(!a){g.B(0);break}if(!a.skipRetry||void 0===a.id){g.B(8);break}return w(g,Tj(a.id),8);case 8:yk(a.url,a.options,!!a.skipRetry),g.h=0}})})}
function Dk(a){var b=this;if(!Ak())throw Mi("updateRequestHandlers");var c=a.options.onError?a.options.onError:function(){};
a.options.onError=function(e,f){return H(b,function h(){return x(h,function(k){switch(k.h){case 1:if(!((B("ytNetworklessLoggingInitializationOptions")?pk.potentialEsfErrorCounter:nk)<=Rf("potential_esf_error_limit",10))){k.B(2);break}return w(k,sk().T(),3);case 3:if(sk().K())B("ytNetworklessLoggingInitializationOptions")&&pk.potentialEsfErrorCounter++,nk++;else return c(e,f),k.return();case 2:if(void 0===(null===a||void 0===a?void 0:a.id)){k.B(4);break}return 1>a.sendCount?w(k,Sj(a.id),8):w(k,Tj(a.id),
4);case 8:ig(function(){sk().K()&&tk()},5E3);
case 4:c(e,f),k.h=0}})})};
var d=a.options.onSuccess?a.options.onSuccess:function(){};
a.options.onSuccess=function(e,f){return H(b,function h(){return x(h,function(k){if(1==k.h)return void 0===(null===a||void 0===a?void 0:a.id)?k.B(2):w(k,Tj(a.id),2);d(e,f);k.h=0})})};
return a}
function Ck(a,b){a=a.timestamp;return P()-a>=b?!1:!0}
function rk(){var a=this;if(!Ak())throw Mi("retryQueuedRequests");Qj("QUEUED").then(function(b){b&&!Ck(b,12E4)?ig(function(){return H(a,function d(){return x(d,function(e){if(1==e.h)return void 0===b.id?e.B(2):w(e,Sj(b.id),2);rk();e.h=0})})}):sk().K()&&tk()})}
function vk(){return H(this,function b(){var c,d;return x(b,function(e){c=Ak();if(!c)throw d=Mi("clearSWHealthLogsDb"),d;return e.return(Zj().catch(function(f){Mf(f)}))})})}
function sk(){ok||(ok=new ik({fb:!0,Ta:!0}));return ok}
function yk(a,b,c){if(O("networkless_with_beacon")){var d=["method","postBody"];if(Object.keys(b).length>d.length)c=!0;else{c=0;d=u(d);for(var e=d.next();!e.done;e=d.next())b.hasOwnProperty(e.value)&&c++;c=Object.keys(b).length!==c}c?Ng(a,b):bh(a,void 0,b.postBody)}else c&&0===Object.keys(b).length?Zg(a):Ng(a,b)}
function xk(){return B("ytNetworklessLoggingInitializationOptions")?pk.isNwlInitialized:kk}
function Ak(){return B("ytNetworklessLoggingInitializationOptions")?pk.databaseToken:lk}
;function Ek(a){var b=this;this.config_=null;a?this.config_=a:Vh()&&(this.config_=Fh());gg(function(){ci(b)},5E3)}
Ek.prototype.isReady=function(){!this.config_&&Vh()&&(this.config_=Fh());return!!this.config_};
function Ih(a,b,c,d){function e(r){r=void 0===r?!1:r;var p;if(d.retry&&"www.youtube-nocookie.com"!=h&&(r||(p=ai(b,c,l,k)),p)){var z=g.onSuccess,I=g.onFetchSuccess;g.onSuccess=function(E,R){bi(p);z(E,R)};
c.onFetchSuccess=function(E,R){bi(p);I(E,R)}}try{r&&d.retry&&!d.La.bypassNetworkless?(g.method="POST",d.La.writeThenSend?wk(q,g):Bk(q,g)):(g.method="POST",g.postParams||(g.postParams={}),Ng(q,g))}catch(E){if("InvalidAccessError"==E.name)p&&(bi(p),p=0),Nf(Error("An extension is blocking network request."));
else throw E;}p&&gg(function(){ci(a)},5E3)}
!F("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&Nf(new xi("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var f=new xi("innertube xhrclient not ready",b,c,d);Mf(f);throw f;}var g={headers:{"Content-Type":"application/json"},method:"POST",postParams:c,postBodyFormat:"JSON",onTimeout:function(){d.onTimeout()},
onFetchTimeout:d.onTimeout,onSuccess:function(r,p){if(d.onSuccess)d.onSuccess(p)},
onFetchSuccess:function(r){if(d.onSuccess)d.onSuccess(r)},
onError:function(r,p){if(d.onError)d.onError(p)},
onFetchError:function(r){if(d.onError)d.onError(r)},
timeout:d.timeout,withCredentials:!0},h="";(f=a.config_.bb)&&(h=f);var k=a.config_.eb||!1,l=Wh(k,h,d);Object.assign(g.headers,l);g.headers.Authorization&&!h&&(g.headers["x-origin"]=window.location.origin);f="/youtubei/"+a.config_.innertubeApiVersion+"/"+b;var n={alt:"json"};a.config_.cb&&g.headers.Authorization||(n.key=a.config_.innertubeApiKey);var q=Bg(""+h+f,n||{},!0);xk()?zj().then(function(r){e(r)}):e(!1)}
;function Fk(a,b,c){c=void 0===c?{}:c;var d=Ek;F("ytLoggingEventsDefaultDisabled",!1)&&Ek==Ek&&(d=null);Kh(a,b,d,c)}
;var Gk=[{za:function(a){return"Cannot read property '"+a.key+"'"},
la:{Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}],TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,
groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]},{regexp:/(null) is not an object \(evaluating '(?:([^.]+)\.)?([^']+)'\)/,groups:["value","base","key"]}]}},{za:function(a){return"Cannot call '"+a.key+"'"},
la:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/([^ ]+) called on (null or undefined)/,groups:["key","value"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,
groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,groups:["key"]}]}},{za:function(a){return a.key+" is not defined"},
la:{ReferenceError:[{regexp:/(.*) is not defined/,groups:["key"]},{regexp:/Can't find variable: (.*)/,groups:["key"]}]}}];var Ik={S:[],O:[{Da:Hk,weight:500}]};function Hk(a){a=a.stack;return a.includes("chrome://")||a.includes("chrome-extension://")||a.includes("moz-extension://")}
;function Jk(){this.O=[];this.S=[]}
var Kk;function Lk(){if(!Kk){var a=Kk=new Jk;a.S.length=0;a.O.length=0;Ik.S&&a.S.push.apply(a.S,Ik.S);Ik.O&&a.O.push.apply(a.O,Ik.O)}return Kk}
;var Mk=new M;function Nk(a){function b(){return a.charCodeAt(d++)}
var c=a.length,d=0;do{var e=Ok(b);if(Infinity===e)break;var f=e>>3;switch(e&7){case 0:e=Ok(b);if(2===f)return e;break;case 1:if(2===f)return;d+=8;break;case 2:e=Ok(b);if(2===f)return a.substr(d,e);d+=e;break;case 5:if(2===f)return;d+=4;break;default:return}}while(d<c)}
function Ok(a){var b=a(),c=b&127;if(128>b)return c;b=a();c|=(b&127)<<7;if(128>b)return c;b=a();c|=(b&127)<<14;if(128>b)return c;b=a();return 128>b?c|(b&127)<<21:Infinity}
;function Pk(a,b,c,d){if(a)if(Array.isArray(a)){var e=d;for(d=0;d<a.length&&!(a[d]&&(e+=Qk(d,a[d],b,c),500<e));d++);d=e}else if("object"===typeof a)for(e in a){if(a[e]){var f=a[e];var g=b;var h=c;g="string"!==typeof f||"clickTrackingParams"!==e&&"trackingParams"!==e?0:(f=Nk(atob(f.replace(/-/g,"+").replace(/_/g,"/"))))?Qk(e+".ve",f,g,h):0;d+=g;d+=Qk(e,a[e],b,c);if(500<d)break}}else c[b]=Rk(a),d+=c[b].length;else c[b]=Rk(a),d+=c[b].length;return d}
function Qk(a,b,c,d){c+="."+a;a=Rk(b);d[c]=a;return c.length+a.length}
function Rk(a){return("string"===typeof a?a:String(JSON.stringify(a))).substr(0,500)}
;var Sk=new Set,Tk=0,Uk=0,Vk=0,Wk=[],Xk=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function Yk(a){Zk(a,"WARNING")}
function Zk(a,b,c,d,e,f){f=void 0===f?{}:f;f.name=c||F("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||F("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);c=f||{};b=void 0===b?"ERROR":b;b=void 0===b?"ERROR":b;if(a&&(a.hasOwnProperty("level")&&a.level&&(b=a.level),O("console_log_js_exceptions")&&(d=[],d.push("Name: "+a.name),d.push("Message: "+a.message),a.hasOwnProperty("params")&&d.push("Error Params: "+JSON.stringify(a.params)),a.hasOwnProperty("args")&&d.push("Error args: "+JSON.stringify(a.args)),d.push("File name: "+
a.fileName),d.push("Stacktrace: "+a.stack),window.console.log(d.join("\n"),a)),!(5<=Tk))){var g=Od(a);d=g.message||"Unknown Error";e=g.name||"UnknownError";var h=g.stack||a.i||"Not available";h.startsWith(e+": "+d)&&(f=h.split("\n"),f.shift(),h=f.join("\n"));f=g.lineNumber||"Not available";g=g.fileName||"Not available";var k=0;if(a.hasOwnProperty("args")&&a.args&&a.args.length)for(var l=0;l<a.args.length&&!(k=Pk(a.args[l],"params."+l,c,k),500<=k);l++);else if(a.hasOwnProperty("params")&&a.params){var n=
a.params;if("object"===typeof a.params)for(l in n){if(n[l]){var q="params."+l,r=Rk(n[l]);c[q]=r;k+=q.length+r.length;if(500<k)break}}else c.params=Rk(n)}if(Wk.length)for(l=0;l<Wk.length&&!(k=Pk(Wk[l],"params.context."+l,c,k),500<=k);l++);navigator.vendor&&!c.hasOwnProperty("vendor")&&(c["device.vendor"]=navigator.vendor);l={message:d,name:e,lineNumber:f,fileName:g,stack:h,params:c,sampleWeight:1};c=Number(a.columnNumber);isNaN(c)||(l.lineNumber=l.lineNumber+":"+c);if("IGNORED"===a.level)a=0;else a:{a=
Lk();c=u(a.S);for(d=c.next();!d.done;d=c.next())if(d=d.value,l.message&&l.message.match(d.Pl)){a=d.weight;break a}a=u(a.O);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.Da(l)){a=c.weight;break a}a=1}l.sampleWeight=a;a=u(Gk);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.la[l.name])for(e=u(c.la[l.name]),d=e.next();!d.done;d=e.next())if(f=d.value,d=l.message.match(f.regexp)){l.params["params.error.original"]=d[0];e=f.groups;f={};for(g=0;g<e.length;g++)f[e[g]]=d[g+1],l.params["params.error."+e[g]]=
d[g+1];l.message=c.za(f);break}l.params||(l.params={});a=Lk();l.params["params.errorServiceSignature"]="msg="+a.S.length+"&cb="+a.O.length;l.params["params.serviceWorker"]="false";y.document&&y.document.querySelectorAll&&(l.params["params.fscripts"]=String(document.querySelectorAll("script:not([nonce])").length));sb("sample").constructor!==qb&&(l.params["params.fconst"]="true");window.yterr&&"function"===typeof window.yterr&&window.yterr(l);if(0!==l.sampleWeight&&!Sk.has(l.message)){"ERROR"===b?(Mk.W("handleError",
l),O("record_app_crashed_web")&&0===Vk&&1===l.sampleWeight&&(Vk++,Fk("appCrashed",{appCrashType:"APP_CRASH_TYPE_BREAKPAD"})),Uk++):"WARNING"===b&&Mk.W("handleWarning",l);if(O("kevlar_gel_error_routing")){a=b;b:{c=u(Xk);for(d=c.next();!d.done;d=c.next())if(Wg(d.value.toLowerCase())){c=!0;break b}c=!1}if(c)c=void 0;else{d={stackTrace:l.stack};l.fileName&&(d.filename=l.fileName);c=l.lineNumber&&l.lineNumber.split?l.lineNumber.split(":"):[];0!==c.length&&(1!==c.length||isNaN(Number(c[0]))?2!==c.length||
isNaN(Number(c[0]))||isNaN(Number(c[1]))||(d.lineNumber=Number(c[0]),d.columnNumber=Number(c[1])):d.lineNumber=Number(c[0]));c={level:"ERROR_LEVEL_UNKNOWN",message:l.message,errorClassName:l.name,sampleWeight:l.sampleWeight};"ERROR"===a?c.level="ERROR_LEVEL_ERROR":"WARNING"===a&&(c.level="ERROR_LEVEL_WARNNING");d={isObfuscated:!0,browserStackInfo:d};e={pageUrl:window.location.href,kvPairs:[]};F("FEXP_EXPERIMENTS")&&(e.experimentIds=F("FEXP_EXPERIMENTS"));if(f=l.params)for(g=u(Object.keys(f)),h=g.next();!h.done;h=
g.next())h=h.value,e.kvPairs.push({key:"client."+h,value:String(f[h])});f=F("SERVER_NAME",void 0);g=F("SERVER_VERSION",void 0);f&&g&&(e.kvPairs.push({key:"server.name",value:f}),e.kvPairs.push({key:"server.version",value:g}));c={errorMetadata:e,stackTrace:d,logMessage:c}}c&&(Fk("clientError",c),("ERROR"===a||O("errors_flush_gel_always_killswitch"))&&Ah())}if(!O("suppress_error_204_logging")){a=l.params||{};b={urlParams:{a:"logerror",t:"jserror",type:l.name,msg:l.message.substr(0,250),line:l.lineNumber,
level:b,"client.name":a.name},postParams:{url:F("PAGE_NAME",window.location.href),file:l.fileName},method:"POST"};a.version&&(b["client.version"]=a.version);if(b.postParams){l.stack&&(b.postParams.stack=l.stack);c=u(Object.keys(a));for(d=c.next();!d.done;d=c.next())d=d.value,b.postParams["client."+d]=a[d];if(a=F("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(c=u(Object.keys(a)),d=c.next();!d.done;d=c.next())d=d.value,b.postParams[d]=a[d];a=F("SERVER_NAME",void 0);c=F("SERVER_VERSION",void 0);
a&&c&&(b.postParams["server.name"]=a,b.postParams["server.version"]=c)}Ng(F("ECATCHER_REPORT_HOST","")+"/error_204",b)}try{Sk.add(l.message)}catch(p){}Tk++}}}
function $k(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];a.args||(a.args=[]);a.args.push.apply(a.args,fa(c))}
;var al={ic:3611,xb:27686,yb:85013,zb:23462,Bb:42016,Cb:62407,Db:26926,Ab:43781,Eb:51236,Fb:79148,Gb:50160,Hb:77504,Tb:87907,Ub:18630,Vb:54445,Wb:80935,Xb:105675,Yb:37521,Zb:47786,ac:98349,cc:123695,dc:6827,ec:29434,fc:7282,hc:124448,lc:32276,kc:76278,mc:93911,nc:106531,oc:27259,pc:27262,qc:27263,tc:21759,uc:27107,wc:62936,xc:49568,yc:38408,zc:80637,Ac:68727,Bc:68728,Cc:80353,Dc:80356,Ec:74610,Fc:45707,Gc:83962,Hc:83970,Ic:46713,Jc:89711,Kc:74612,Lc:93265,Mc:74611,Nc:131380,Pc:128979,Qc:128978,Oc:131391,
Rc:105350,Tc:134800,Sc:131392,Vc:113533,Wc:93252,Xc:99357,Zc:94521,bd:114252,cd:113532,dd:94522,Yc:94583,ed:88E3,fd:93253,gd:93254,hd:94387,jd:94388,kd:93255,ld:97424,Uc:72502,md:110111,nd:76019,pd:117092,qd:117093,od:89431,rd:110466,sd:77240,td:60508,ud:73393,vd:113534,wd:92098,xd:131381,yd:84517,zd:83759,Ad:80357,Bd:86113,Cd:72598,Dd:72733,Ed:107349,Fd:124275,Gd:118203,Hd:133275,Id:133274,Jd:133272,Kd:133273,Ld:133276,Nd:117431,Md:133797,Od:128572,Pd:133405,Qd:117429,Rd:117430,Sd:117432,Td:120080,
Ud:117259,Vd:121692,Wd:132972,Xd:133051,Yd:133658,Zd:132971,ae:97615,be:31402,de:133624,ee:133623,ge:133622,ce:133621,he:84774,ie:95117,je:98930,ke:98931,le:98932,me:43347,ne:129889,oe:45474,pe:100352,qe:84758,re:98443,se:117985,te:74613,ue:74614,we:64502,xe:74615,ye:74616,ze:122224,Ae:74617,Be:77820,Ce:74618,De:93278,Ee:93274,Fe:93275,Ge:93276,He:22110,Ie:29433,Je:133798,Ke:132295,Me:120541,Oe:82047,Pe:113550,Qe:75836,Re:75837,Se:42352,Te:84512,Ue:76065,Ve:75989,We:16623,Xe:32594,Ye:27240,Ze:32633,
af:74858,cf:3945,bf:16989,df:45520,ef:25488,ff:25492,gf:25494,hf:55760,jf:14057,kf:18451,lf:57204,mf:57203,nf:17897,pf:57205,qf:18198,rf:17898,sf:17909,tf:43980,uf:46220,vf:11721,wf:49954,xf:96369,yf:3854,zf:56251,Af:25624,Bf:16906,Cf:99999,Df:68172,Ef:27068,Ff:47973,Gf:72773,Hf:26970,If:26971,Jf:96805,Kf:17752,Lf:73233,Mf:109512,Nf:22256,Of:14115,Pf:22696,Qf:89278,Rf:89277,Sf:109513,Tf:43278,Uf:43459,Vf:43464,Wf:89279,Xf:43717,Yf:55764,Zf:22255,ag:89281,cg:40963,dg:43277,eg:43442,fg:91824,gg:120137,
hg:96367,ig:36850,jg:72694,kg:37414,lg:36851,ng:124863,mg:121343,og:73491,pg:54473,qg:43375,rg:46674,sg:32473,tg:72901,ug:72906,vg:50947,wg:50612,xg:50613,yg:50942,zg:84938,Ag:84943,Bg:84939,Cg:84941,Dg:84944,Eg:84940,Fg:84942,Gg:35585,Hg:51926,Ig:79983,Jg:63238,Kg:18921,Lg:63241,Mg:57893,Ng:41182,Og:33424,Pg:22207,Qg:42993,Rg:36229,Sg:22206,Tg:22205,Ug:18993,Vg:19001,Wg:18990,Xg:18991,Yg:18997,Zg:18725,ah:19003,bh:36874,dh:44763,eh:33427,fh:67793,gh:22182,hh:37091,ih:34650,jh:50617,kh:47261,lh:22287,
mh:25144,nh:97917,oh:62397,ph:125598,qh:36961,rh:108035,sh:27426,th:27857,uh:27846,vh:27854,wh:69692,xh:61411,yh:39299,zh:38696,Ah:62520,Bh:36382,Ch:108701,Dh:50663,Eh:36387,Fh:14908,Gh:37533,Hh:105443,Ih:61635,Jh:62274,Kh:133818,Lh:65702,Mh:65703,Nh:65701,Oh:76256,Ph:37671,Qh:49953,Sh:36216,Th:28237,Uh:39553,Vh:29222,Wh:26107,Xh:38050,Yh:26108,ai:120745,Zh:26109,bi:26110,ci:66881,di:28236,fi:14586,gi:57929,hi:74723,ii:44098,ji:44099,mi:23528,ni:61699,ki:134104,li:134103,oi:59149,ri:101951,si:97346,
ti:118051,vi:95102,wi:64882,xi:119505,yi:63595,zi:63349,Ai:95101,Bi:75240,Ci:27039,Di:68823,Ei:21537,Fi:83464,Gi:75707,Hi:83113,Ii:101952,Ji:101953,Li:79610,Mi:125755,Ni:24402,Oi:24400,Pi:32925,Qi:57173,Ri:122502,Si:64423,Ti:64424,Ui:33986,Vi:100828,Wi:129089,Xi:21409,Yi:11070,Zi:11074,aj:17880,bj:14001,dj:30709,ej:30707,fj:30711,gj:30710,hj:30708,cj:26984,ij:63648,jj:63649,kj:51879,lj:111059,mj:5754,nj:20445,pj:130975,oj:130976,qj:110386,rj:113746,sj:66557,tj:17310,uj:28631,vj:21589,wj:68012,xj:60480,
yj:31571,zj:76980,Aj:41577,Bj:45469,Cj:38669,Dj:13768,Ej:13777,Fj:62985,Gj:4724,Hj:59369,Ij:43927,Jj:43928,Kj:12924,Lj:100355,Oj:56219,Pj:27669,Qj:10337,Nj:47896,Rj:122629,Sj:121258,Tj:107598,Uj:127991,Vj:96639,Wj:107536,Xj:130169,Yj:96661,Zj:96658,ak:116646,bk:121122,ck:96660,dk:127738,ek:127083,fk:104443,gk:96659,hk:106442,ik:134840,jk:63667,kk:63668,lk:63669,mk:130686,nk:78314,pk:55761,qk:127098,rk:134841,sk:96368,tk:67374,uk:48992,vk:49956,wk:31961,xk:26388,yk:23811,zk:5E4,Ak:126250,Bk:96370,
Ck:47355,Dk:47356,Ek:37935,Fk:45521,Gk:21760,Hk:83769,Ik:49977,Jk:49974,Kk:93497,Lk:93498,Mk:34325,Nk:115803,Ok:123707,Pk:100081,Qk:35309,Rk:68314,Sk:25602,Tk:100339,Uk:59018,Vk:18248,Wk:50625,Xk:9729,Yk:37168,Zk:37169,al:21667,bl:16749,dl:18635,fl:39305,il:18046,jl:53969,kl:8213,ll:93926,ml:102852,nl:110099,ol:22678,pl:69076,rl:100856,sl:17736,ul:3832,vl:55759,wl:64031,xl:93044,yl:93045,zl:34388,Al:17657,Bl:17655,Cl:39579,Dl:39578,El:77448,Fl:8196,Gl:11357,Hl:69877,Il:8197,Jl:82039};function bl(){var a=kb(cl),b;return bf(new Ve(function(c,d){a.onSuccess=function(e){Hg(e)?c(new dl(e)):d(new el("Request failed, status="+(e&&"status"in e?e.status:-1),"net.badstatus",e))};
a.onError=function(e){d(new el("Unknown request error","net.unknown",e))};
a.onTimeout=function(e){d(new el("Request timed out","net.timeout",e))};
b=Ng("//googleads.g.doubleclick.net/pagead/id",a)}),function(c){c instanceof cf&&b.abort();
return $e(c)})}
function el(a,b,c){Ta.call(this,a+", errorCode="+b);this.errorCode=b;this.xhr=c;this.name="PromiseAjaxError"}
v(el,Ta);function dl(a){this.xhr=a}
;function fl(){this.i=0;this.h=null}
fl.prototype.then=function(a,b,c){return 1===this.i&&a?(a=a.call(c,this.h),Ue(a)?a:gl(a)):2===this.i&&b?(a=b.call(c,this.h),Ue(a)?a:hl(a)):this};
fl.prototype.getValue=function(){return this.h};
fl.prototype.$goog_Thenable=!0;function hl(a){var b=new fl;a=void 0===a?null:a;b.i=2;b.h=void 0===a?null:a;return b}
function gl(a){var b=new fl;a=void 0===a?null:a;b.i=1;b.h=void 0===a?null:a;return b}
;function il(){if(qd())return!0;var a=F("INNERTUBE_CLIENT_NAME");return!a||"WEB"!==a&&"MWEB"!==a||Vg&&Wg("applewebkit")&&!Wg("version")&&(!Wg("safari")||Wg("gsa/"))||pc&&Wg("version/")?!0:(a=od.get("CONSENT",void 0))?a.startsWith("YES+"):!0}
;function jl(a){Ta.call(this,a.message||a.description||a.name);this.isMissing=a instanceof kl;this.isTimeout=a instanceof el&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof cf}
v(jl,Ta);jl.prototype.name="BiscottiError";function kl(){Ta.call(this,"Biscotti ID is missing from server")}
v(kl,Ta);kl.prototype.name="BiscottiMissingError";var cl={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},ll=null;function rg(){if(O("disable_biscotti_fetch_entirely_for_all_web_clients"))return $e(Error("Biscotti id fetching has been disabled entirely."));if(!il())return $e(Error("User has not consented - not fetching biscotti id."));if("1"==ib())return $e(Error("Biscotti ID is not available in private embed mode"));ll||(ll=bf(bl().then(ml),function(a){return nl(2,a)}));
return ll}
function ml(a){a=a.xhr.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new kl;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new kl;a=a.id;sg(a);ll=gl(a);ol(18E5,2);return a}
function nl(a,b){b=new jl(b);sg("");ll=hl(b);0<a&&ol(12E4,a-1);throw b;}
function ol(a,b){cg(function(){bf(bl().then(ml,function(c){return nl(b,c)}),Ea)},a)}
function pl(){try{var a=B("yt.ads.biscotti.getId_");return a?a():rg()}catch(b){return $e(b)}}
;function ql(a){if("1"!=ib()){a&&qg();try{pl().then(function(){},function(){}),cg(ql,18E5)}catch(b){Mf(b)}}}
;var rl=Date.now().toString();
function sl(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=Date.now();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(rl)for(a=1,b=0;b<rl.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^rl.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));
return a.join("")}
;var tl,ul=y.ytLoggingDocDocumentNonce_;ul||(ul=sl(),Ra("ytLoggingDocDocumentNonce_",ul));tl=ul;var vl={Le:0,jc:1,sc:2,Rh:3,Ne:4,ql:5,Ki:6,Mj:7,0:"DEFAULT",1:"CHAT",2:"CONVERSATIONS",3:"MINIPLAYER",4:"DIALOG",5:"VOZ",6:"MUSIC_WATCH_TABS",7:"SHARE"};function wl(a){this.h=a}
function xl(a){return new wl({trackingParams:a})}
wl.prototype.getAsJson=function(){var a={};void 0!==this.h.trackingParams?a.trackingParams=this.h.trackingParams:(a.veType=this.h.veType,void 0!==this.h.veCounter&&(a.veCounter=this.h.veCounter),void 0!==this.h.elementIndex&&(a.elementIndex=this.h.elementIndex));void 0!==this.h.dataElement&&(a.dataElement=this.h.dataElement.getAsJson());void 0!==this.h.youtubeData&&(a.youtubeData=this.h.youtubeData);return a};
wl.prototype.toString=function(){return JSON.stringify(this.getAsJson())};
wl.prototype.isClientVe=function(){return!this.h.trackingParams&&!!this.h.veType};function yl(a){a=void 0===a?0:a;return 0==a?"client-screen-nonce":"client-screen-nonce."+a}
function zl(a){a=void 0===a?0:a;return 0==a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a}
function Al(a){return F(zl(void 0===a?0:a),void 0)}
A("yt_logging_screen.getRootVeType",Al,void 0);function Bl(a){return(a=Al(void 0===a?0:a))?new wl({veType:a,youtubeData:void 0}):null}
function Cl(){var a=F("csn-to-ctt-auth-info");a||(a={},N("csn-to-ctt-auth-info",a));return a}
function Dl(a){a=void 0===a?0:a;var b=F(yl(a));if(!b&&!F("USE_CSN_FALLBACK",!0))return null;b||!O("use_undefined_csn_any_layer")&&0!=a||(b="UNDEFINED_CSN");return b?b:null}
A("yt_logging_screen.getCurrentCsn",Dl,void 0);function El(a,b,c){var d=Cl();(c=Dl(c))&&delete d[c];b&&(d[a]=b)}
function Fl(a){return Cl()[a]}
A("yt_logging_screen.getCttAuthInfo",Fl,void 0);function Gl(a,b,c,d){c=void 0===c?0:c;if(a!==F(yl(c))||b!==F(zl(c)))El(a,d,c),N(yl(c),a),N(zl(c),b),b=function(){setTimeout(function(){a&&Kh("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:tl,clientScreenNonce:a},Ek)},0)},"requestAnimationFrame"in window?window.requestAnimationFrame(b):b()}
A("yt_logging_screen.setCurrentScreen",Gl,void 0);function Hl(a){di.call(this,1,arguments);this.csn=a}
v(Hl,di);var mi=new ei("screen-created",Hl),Il=[],Kl=Jl,Ll=0;function Ml(a,b,c,d){var e=d.filter(function(f){f.csn!==b?(f.csn=b,f=!0):f=!1;return f});
c={csn:b,parentVe:c.getAsJson(),childVes:Ya(e,function(f){return f.getAsJson()})};
d=u(d);for(e=d.next();!e.done;e=d.next())e=e.value.getAsJson(),(gb(e)||!e.trackingParams&&!e.veType)&&Yk(Error("Child VE logged with no data"));d={cttAuthInfo:Fl(b),U:b};"UNDEFINED_CSN"==b?Nl("visualElementAttached",c,d):a?Kh("visualElementAttached",c,a,d):Fk("visualElementAttached",c,d)}
function Jl(){for(var a=Math.random()+"",b=[],c=0,d=0;d<a.length;d++){var e=a.charCodeAt(d);255<e&&(b[c++]=e&255,e>>=8);b[c++]=e}return Ec(b)}
function Nl(a,b,c){Il.push({payloadName:a,payload:b,options:c});Ll||(Ll=ni())}
function oi(a){if(Il){for(var b=u(Il),c=b.next();!c.done;c=b.next())c=c.value,c.payload&&(c.payload.csn=a.csn,Kh(c.payloadName,c.payload,null,c.options));Il.length=0}Ll=0}
;function Ol(){this.i=new Set;this.h=new Set;this.j=new Map}
Ol.prototype.clear=function(){this.i.clear();this.h.clear();this.j.clear()};
Fa(Ol);function Pl(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];if(!Ql(a)||c.some(function(e){return!Ql(e)}))throw Error("Only objects may be merged.");
c=u(c);for(d=c.next();!d.done;d=c.next())Rl(a,d.value);return a}
function Rl(a,b){for(var c in b)if(Ql(b[c])){if(c in a&&!Ql(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});Rl(a[c],b[c])}else if(Sl(b[c])){if(c in a&&!Sl(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);Tl(a[c],b[c])}else a[c]=b[c];return a}
function Tl(a,b){b=u(b);for(var c=b.next();!c.done;c=b.next())c=c.value,Ql(c)?a.push(Rl({},c)):Sl(c)?a.push(Tl([],c)):a.push(c);return a}
function Ql(a){return"object"===typeof a&&!Array.isArray(a)}
function Sl(a){return"object"===typeof a&&Array.isArray(a)}
;function Ul(a,b){di.call(this,1,arguments)}
v(Ul,di);function Vl(a,b){di.call(this,1,arguments)}
v(Vl,di);var Wl=new ei("aft-recorded",Ul),Xl=new ei("timing-sent",Vl);var Yl=window;function Zl(){this.timing={};this.clearResourceTimings=function(){};
this.webkitClearResourceTimings=function(){};
this.mozClearResourceTimings=function(){};
this.msClearResourceTimings=function(){};
this.oClearResourceTimings=function(){}}
var W=Yl.performance||Yl.mozPerformance||Yl.msPerformance||Yl.webkitPerformance||new Zl;var $l=!1,am={'script[name="scheduler/scheduler"]':"sj",'script[name="player/base"]':"pj",'link[rel="stylesheet"][name="www-player"]':"pc",'link[rel="stylesheet"][name="player/www-player"]':"pc",'script[name="desktop_polymer/desktop_polymer"]':"dpj",'link[rel="import"][name="desktop_polymer"]':"dph",'script[name="mobile-c3"]':"mcj",'link[rel="stylesheet"][name="mobile-c3"]':"mcc",'script[name="player-plasma-ias-phone/base"]':"mcppj",'script[name="player-plasma-ias-tablet/base"]':"mcptj",'link[rel="stylesheet"][name="mobile-polymer-player-ias"]':"mcpc",
'link[rel="stylesheet"][name="mobile-polymer-player-svg-ias"]':"mcpsc",'script[name="mobile_blazer_core_mod"]':"mbcj",'link[rel="stylesheet"][name="mobile_blazer_css"]':"mbc",'script[name="mobile_blazer_logged_in_users_mod"]':"mbliuj",'script[name="mobile_blazer_logged_out_users_mod"]':"mblouj",'script[name="mobile_blazer_noncore_mod"]':"mbnj","#player_css":"mbpc",'script[name="mobile_blazer_desktopplayer_mod"]':"mbpj",'link[rel="stylesheet"][name="mobile_blazer_tablet_css"]':"mbtc",'script[name="mobile_blazer_watch_mod"]':"mbwj"};
Pa(W.clearResourceTimings||W.webkitClearResourceTimings||W.mozClearResourceTimings||W.msClearResourceTimings||W.oClearResourceTimings||Ea,W);function bm(a){var b=cm(a);if(b.aft)return b.aft;a=F((a||"")+"TIMING_AFT_KEYS",["ol"]);for(var c=a.length,d=0;d<c;d++){var e=b[a[d]];if(e)return e}return NaN}
function dm(){var a;if(O("csi_use_performance_navigation_timing")){var b,c,d,e=null===(d=null===(c=null===(b=null===(a=null===W||void 0===W?void 0:W.getEntriesByType)||void 0===a?void 0:a.call(W,"navigation"))||void 0===b?void 0:b[0])||void 0===c?void 0:c.toJSON)||void 0===d?void 0:d.call(c);e?(e.requestStart=em(e.requestStart),e.responseEnd=em(e.responseEnd),e.redirectStart=em(e.redirectStart),e.redirectEnd=em(e.redirectEnd),e.domainLookupEnd=em(e.domainLookupEnd),e.connectStart=em(e.connectStart),
e.connectEnd=em(e.connectEnd),e.responseStart=em(e.responseStart),e.secureConnectionStart=em(e.secureConnectionStart),e.domainLookupStart=em(e.domainLookupStart),e.isPerformanceNavigationTiming=!0,a=e):a=W.timing}else a=W.timing;return a}
function fm(){return O("csi_use_time_origin")&&W.timeOrigin?Math.floor(W.timeOrigin):W.timing.navigationStart}
function em(a){return Math.round(fm()+a)}
function gm(a){var b;(b=B("ytcsi."+(a||"")+"data_"))||(b={tick:{},info:{}},Ra("ytcsi."+(a||"")+"data_",b));return b}
function hm(a){a=gm(a);a.info||(a.info={});return a.info}
function cm(a){a=gm(a);a.tick||(a.tick={});return a.tick}
function im(a){var b=gm(a).nonce;b||(b=sl(),gm(a).nonce=b);return b}
function jm(a){var b=cm(a||""),c=bm(a);c&&!$l&&(ji(Wl,new Ul(Math.round(c-b._start),a)),$l=!0)}
;function km(){if(W.getEntriesByType){var a=W.getEntriesByType("paint");if(a=$a(a,function(b){return"first-paint"===b.name}))return em(a.startTime)}a=W.timing;
return a.ib?Math.max(0,a.ib):0}
;function lm(){var a=B("ytcsi.debug");a||(a=[],A("ytcsi.debug",a,void 0),A("ytcsi.reference",{},void 0));return a}
function mm(a){a=a||"";var b=B("ytcsi.reference");b||(lm(),b=B("ytcsi.reference"));if(b[a])return b[a];var c=lm(),d={timerName:a,info:{},tick:{},span:{}};c.push(d);return b[a]=d}
;var nm=y.ytLoggingLatencyUsageStats_||{};A("ytLoggingLatencyUsageStats_",nm,void 0);function om(){this.h=0}
function pm(){om.h||(om.h=new om);return om.h}
om.prototype.tick=function(a,b,c,d){qm(this,"tick_"+a+"_"+b)||Fk("latencyActionTicked",{tickName:a,clientActionNonce:b},{timestamp:c,cttAuthInfo:d})};
om.prototype.info=function(a,b,c){var d=Object.keys(a).join("");qm(this,"info_"+d+"_"+b)||(a=Object.assign({},a),a.clientActionNonce=b,Fk("latencyActionInfo",a,{cttAuthInfo:c}))};
om.prototype.span=function(a,b,c){var d=Object.keys(a).join("");qm(this,"span_"+d+"_"+b)||(a.clientActionNonce=b,Fk("latencyActionSpan",a,{cttAuthInfo:c}))};
function qm(a,b){nm[b]=nm[b]||{count:0};var c=nm[b];c.count++;c.time=P();a.h||(a.h=gg(function(){var d=P(),e;for(e in nm)nm[e]&&6E4<d-nm[e].time&&delete nm[e];a&&(a.h=0)},5E3));
return 5<c.count?(6===c.count&&1>1E5*Math.random()&&(c=new xi("CSI data exceeded logging limit with key",b.split("_")),0<=b.indexOf("plev")||Yk(c)),!0):!1}
;var X={},rm=(X.auto_search="LATENCY_ACTION_AUTO_SEARCH",X.ad_to_ad="LATENCY_ACTION_AD_TO_AD",X.ad_to_video="LATENCY_ACTION_AD_TO_VIDEO",X["analytics.explore"]="LATENCY_ACTION_CREATOR_ANALYTICS_EXPLORE",X.app_startup="LATENCY_ACTION_APP_STARTUP",X["artist.analytics"]="LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS",X["artist.events"]="LATENCY_ACTION_CREATOR_ARTIST_CONCERTS",X["artist.presskit"]="LATENCY_ACTION_CREATOR_ARTIST_PROFILE",X.browse="LATENCY_ACTION_BROWSE",X.channels="LATENCY_ACTION_CHANNELS",X.creator_channel_dashboard=
"LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD",X["channel.analytics"]="LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS",X["channel.comments"]="LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS",X["channel.content"]="LATENCY_ACTION_CREATOR_POST_LIST",X["channel.copyright"]="LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT",X["channel.editing"]="LATENCY_ACTION_CREATOR_CHANNEL_EDITING",X["channel.monetization"]="LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION",X["channel.music"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC",X["channel.playlists"]=
"LATENCY_ACTION_CREATOR_CHANNEL_PLAYLISTS",X["channel.translations"]="LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS",X["channel.videos"]="LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS",X["channel.live_streaming"]="LATENCY_ACTION_CREATOR_LIVE_STREAMING",X.chips="LATENCY_ACTION_CHIPS",X["dialog.copyright_strikes"]="LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES",X["dialog.uploads"]="LATENCY_ACTION_CREATOR_DIALOG_UPLOADS",X.direct_playback="LATENCY_ACTION_DIRECT_PLAYBACK",X.embed="LATENCY_ACTION_EMBED",X.entity_key_serialization_perf=
"LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF",X.entity_key_deserialization_perf="LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF",X.explore="LATENCY_ACTION_EXPLORE",X.home="LATENCY_ACTION_HOME",X.library="LATENCY_ACTION_LIBRARY",X.live="LATENCY_ACTION_LIVE",X.live_pagination="LATENCY_ACTION_LIVE_PAGINATION",X.onboarding="LATENCY_ACTION_ONBOARDING",X.parent_profile_settings="LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS",X.parent_tools_collection="LATENCY_ACTION_PARENT_TOOLS_COLLECTION",X.parent_tools_dashboard=
"LATENCY_ACTION_PARENT_TOOLS_DASHBOARD",X.player_att="LATENCY_ACTION_PLAYER_ATTESTATION",X["post.comments"]="LATENCY_ACTION_CREATOR_POST_COMMENTS",X["post.edit"]="LATENCY_ACTION_CREATOR_POST_EDIT",X.prebuffer="LATENCY_ACTION_PREBUFFER",X.prefetch="LATENCY_ACTION_PREFETCH",X.profile_settings="LATENCY_ACTION_KIDS_PROFILE_SETTINGS",X.profile_switcher="LATENCY_ACTION_LOGIN",X.reel_watch="LATENCY_ACTION_REEL_WATCH",X.results="LATENCY_ACTION_RESULTS",X.search_ui="LATENCY_ACTION_SEARCH_UI",X.search_suggest=
"LATENCY_ACTION_SUGGEST",X.search_zero_state="LATENCY_ACTION_SEARCH_ZERO_STATE",X.secret_code="LATENCY_ACTION_KIDS_SECRET_CODE",X.seek="LATENCY_ACTION_PLAYER_SEEK",X.settings="LATENCY_ACTION_SETTINGS",X.tenx="LATENCY_ACTION_TENX",X.video_to_ad="LATENCY_ACTION_VIDEO_TO_AD",X.watch="LATENCY_ACTION_WATCH",X.watch_it_again="LATENCY_ACTION_KIDS_WATCH_IT_AGAIN",X["watch,watch7"]="LATENCY_ACTION_WATCH",X["watch,watch7_html5"]="LATENCY_ACTION_WATCH",X["watch,watch7ad"]="LATENCY_ACTION_WATCH",X["watch,watch7ad_html5"]=
"LATENCY_ACTION_WATCH",X.wn_comments="LATENCY_ACTION_LOAD_COMMENTS",X.ww_rqs="LATENCY_ACTION_WHO_IS_WATCHING",X["video.analytics"]="LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS",X["video.comments"]="LATENCY_ACTION_CREATOR_VIDEO_COMMENTS",X["video.edit"]="LATENCY_ACTION_CREATOR_VIDEO_EDIT",X["video.editor"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR",X["video.editor_async"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC",X["video.live_settings"]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_SETTINGS",X["video.live_streaming"]=
"LATENCY_ACTION_CREATOR_VIDEO_LIVE_STREAMING",X["video.monetization"]="LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION",X["video.translations"]="LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS",X.voice_assistant="LATENCY_ACTION_VOICE_ASSISTANT",X.cast_load_by_entity_to_watch="LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH",X.networkless_performance="LATENCY_ACTION_NETWORKLESS_PERFORMANCE",X),Y={},sm=(Y.ad_allowed="adTypesAllowed",Y.yt_abt="adBreakType",Y.ad_cpn="adClientPlaybackNonce",Y.ad_docid="adVideoId",Y.yt_ad_an=
"adNetworks",Y.ad_at="adType",Y.aida="appInstallDataAgeMs",Y.aac_type="tvAppInfo.authAccessCredentialType",Y.browse_id="browseId",Y.p="httpProtocol",Y.t="transportProtocol",Y.cs="commandSource",Y.cpn="clientPlaybackNonce",Y.ccs="creatorInfo.creatorCanaryState",Y.csn="clientScreenNonce",Y.docid="videoId",Y.GetHome_rid="requestIds",Y.GetSearch_rid="requestIds",Y.GetPlayer_rid="requestIds",Y.GetWatchNext_rid="requestIds",Y.GetBrowse_rid="requestIds",Y.GetLibrary_rid="requestIds",Y.is_continuation="isContinuation",
Y.is_nav="isNavigation",Y.b_p="kabukiInfo.browseParams",Y.is_prefetch="kabukiInfo.isPrefetch",Y.is_secondary_nav="kabukiInfo.isSecondaryNav",Y.nav_type="kabukiInfo.navigationType",Y.prev_browse_id="kabukiInfo.prevBrowseId",Y.query_source="kabukiInfo.querySource",Y.voz_type="kabukiInfo.vozType",Y.yt_lt="loadType",Y.mver="creatorInfo.measurementVersion",Y.yt_ad="isMonetized",Y.nr="webInfo.navigationReason",Y.nrsu="navigationRequestedSameUrl",Y.ncnp="webInfo.nonPreloadedNodeCount",Y.pnt="performanceNavigationTiming",
Y.prt="playbackRequiresTap",Y.plt="playerInfo.playbackType",Y.pis="playerInfo.playerInitializedState",Y.paused="playerInfo.isPausedOnLoad",Y.yt_pt="playerType",Y.fmt="playerInfo.itag",Y.yt_pl="watchInfo.isPlaylist",Y.yt_pre="playerInfo.preloadType",Y.yt_ad_pr="prerollAllowed",Y.pa="previousAction",Y.yt_red="isRedSubscriber",Y.rce="mwebInfo.responseContentEncoding",Y.rc="resourceInfo.resourceCache",Y.scrh="screenHeight",Y.scrw="screenWidth",Y.st="serverTimeMs",Y.ssdm="shellStartupDurationMs",Y.br_trs=
"tvInfo.bedrockTriggerState",Y.kebqat="kabukiInfo.earlyBrowseRequestInfo.abandonmentType",Y.kebqa="kabukiInfo.earlyBrowseRequestInfo.adopted",Y.label="tvInfo.label",Y.is_mdx="tvInfo.isMdx",Y.preloaded="tvInfo.isPreloaded",Y.upg_player_vis="playerInfo.visibilityState",Y.query="unpluggedInfo.query",Y.upg_chip_ids_string="unpluggedInfo.upgChipIdsString",Y.yt_vst="videoStreamType",Y.vph="viewportHeight",Y.vpw="viewportWidth",Y.yt_vis="isVisible",Y.rcl="mwebInfo.responseContentLength",Y.GetSettings_rid=
"requestIds",Y.GetTrending_rid="requestIds",Y.GetMusicSearchSuggestions_rid="requestIds",Y.REQUEST_ID="requestIds",Y),tm="isContinuation isNavigation kabukiInfo.earlyBrowseRequestInfo.adopted kabukiInfo.isPrefetch kabukiInfo.isSecondaryNav isMonetized navigationRequestedSameUrl performanceNavigationTiming playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber tvInfo.isMdx tvInfo.isPreloaded isVisible watchInfo.isPlaylist playbackRequiresTap".split(" "),um={},vm=(um.ccs="CANARY_STATE_",um.mver="MEASUREMENT_VERSION_",
um.pis="PLAYER_INITIALIZED_STATE_",um.yt_pt="LATENCY_PLAYER_",um.pa="LATENCY_ACTION_",um.yt_vst="VIDEO_STREAM_TYPE_",um),wm="all_vc ap aq c cbr cbrand cbrver cmodel cos cplatform ctheme cver ei l_an l_mm plid srt yt_fss yt_li vpst vpni2 vpil2 icrc icrt pa GetAccountOverview_rid GetHistory_rid cmt d_vpct d_vpnfi d_vpni nsru pc pfa pfeh pftr pnc prerender psc rc start tcrt tcrc ssr vpr vps yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis ytu_pvis yt_ref yt_sts tds".split(" ");
function xm(a){return!!F("FORCE_CSI_ON_GEL",!1)||O("csi_on_gel")||O("enable_csi_on_gel")||O("unplugged_tvhtml5_csi_on_gel")||!!gm(a).useGel}
function ym(a,b,c){var d=zm(c);d.gelTicks&&(d.gelTicks["tick_"+a]=!0);c||b||P();if(xm(c)){mm(c||"").tick[a]=b||P();d=im(c);var e=gm(c).cttAuthInfo;"_start"===a?(a=pm(),qm(a,"baseline_"+d)||Fk("latencyActionBaselined",{clientActionNonce:d},{timestamp:b,cttAuthInfo:e})):pm().tick(a,d,b,e);jm(c);return!0}return!1}
function Am(a,b,c){c=zm(c);if(c.gelInfos)c.gelInfos["info_"+a]=!0;else{var d={};c.gelInfos=(d["info_"+a]=!0,d)}if(a.match("_rid")){var e=a.split("_rid")[0];a="REQUEST_ID"}if(a in sm){c=sm[a];0<=Wa(tm,c)&&(b=!!b);a in vm&&"string"===typeof b&&(b=vm[a]+b.toUpperCase());a=b;b=c.split(".");for(var f=d={},g=0;g<b.length-1;g++){var h=b[g];f[h]={};f=f[h]}f[b[b.length-1]]="requestIds"===c?[{id:a,endpoint:e}]:a;return Pl({},d)}0<=Wa(wm,a)||Yk(new xi("Unknown label logged with GEL CSI",a))}
function zm(a){a=gm(a);if(a.gel){var b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}else a.gel={gelTicks:{},gelInfos:{}};return a.gel}
function Bm(a){a=zm(a);a.gelInfos||(a.gelInfos={});return a.gelInfos}
;function Cm(a,b,c){null!==b&&(hm(c)[a]=b,xm(c)?(a=Am(a,b,c))&&xm(c)&&(b=mm(c||""),Pl(b.info,a),Pl(Bm(c),a),b=im(c),c=gm(c).cttAuthInfo,pm().info(a,b,c)):mm(c||"").info[a]=b)}
function Z(a,b,c){var d=cm(c);if(!b&&"_"!==a[0]){var e=a;W.mark&&(0==e.lastIndexOf("mark_",0)||(e="mark_"+e),c&&(e+=" ("+c+")"),W.mark(e))}e=b||P();d[a]=e;ym(a,b,c)||c||(Dm(),mm("").tick[a]=b||P());return d[a]}
function Em(){var a=im(void 0);requestAnimationFrame(function(){setTimeout(function(){a===im(void 0)&&Z("ol",void 0,void 0)},0)})}
function Dm(){if(!B("yt.timing.pingSent_")){var a=F("TIMING_ACTION",void 0),b=cm();if(a=!!B("ytglobal.timingready_")&&a)a="_start"in cm(void 0);if(a&&bm()){jm();a=!0;var c=F("TIMING_WAIT",[]);if(c.length)for(var d=0,e=c.length;d<e;++d)if(!(c[d]in b)){a=!1;break}if(a&&!xm()){c=cm();d=hm();e=c._start;var f=F("CSI_SERVICE_NAME","youtube");a={v:2,s:f,action:F("TIMING_ACTION",void 0)};b=d.srt;void 0!==c.srt&&delete d.srt;c.aft=bm();var g=cm(void 0),h=g.pbr,k=g.vc;g=g.pbs;h&&k&&g&&h<k&&k<g&&hm(void 0).yt_pvis&&
"youtube"===f&&(Cm("yt_lt","hot_bg"),f=c.vc,h=c.pbs,delete c.aft,d.aft=Math.round(h-f));for(var l in d)"_"!==l.charAt(0)&&(a[l]=d[l]);c.ps=P();l={};f=[];for(var n in c)"_"!==n.charAt(0)&&(h=Math.round(c[n]-e),l[n]=h,f.push(n+"."+h));a.rt=f.join(",");n=!!d.ap;c="";for(var q in a)a.hasOwnProperty(q)&&(c+="&"+q+"="+a[q]);q="/csi_204?"+c.substring(1);window.navigator&&n?bh(q):Zg(q);A("yt.timing.pingSent_",!0,void 0);ji(Xl,new Vl(l.aft+(Number(b)||0)))}}}}
function Fm(){var a=document;if("visibilityState"in a)a=a.visibilityState;else{var b=Tf+"VisibilityState";a=b in a?a[b]:void 0}switch(a){case "hidden":return 0;case "visible":return 1;case "prerender":return 2;case "unloaded":return 3;default:return-1}}
function Gm(a,b){a=document.querySelector(a);if(!a)return!1;var c="",d=a.nodeName;"SCRIPT"===d?(c=a.src,c||(c=a.getAttribute("data-timing-href"))&&(c=window.location.protocol+c)):"LINK"===d&&(c=a.href);Zb()&&a.setAttribute("nonce",Zb());return c?(a=W.getEntriesByName(c))&&a[0]&&(a=a[0],c=fm(),Z("rsf_"+b,c+Math.round(a.fetchStart)),Z("rse_"+b,c+Math.round(a.responseEnd)),void 0!==a.transferSize&&0===a.transferSize)?!0:!1:!1}
function Hm(){var a=window.location.protocol,b=W.getEntriesByType("resource");b=Xa(b,function(c){return 0===c.name.indexOf(a+"//fonts.gstatic.com/s/")});
(b=Za(b,function(c,d){return d.duration>c.duration?d:c},{duration:0}))&&0<b.startTime&&0<b.responseEnd&&(Z("wffs",em(b.startTime)),Z("wffe",em(b.responseEnd)))}
var Im=window;Im.ytcsi&&(Im.ytcsi.info=Cm,Im.ytcsi.tick=Z);function Jm(){this.u=[];this.o=[];this.h=[];this.l=[];this.m=[];this.i=new Set;this.A=new Map}
function Km(a,b,c){c=void 0===c?0:c;b.then(function(d){var e,f;a.i.has(c)&&a.j&&a.j();var g=Dl(c),h=Bl(c);g&&h&&((null===(e=d.response)||void 0===e?0:e.trackingParams)&&Ml(a.client,g,h,[xl(d.response.trackingParams)]),(null===(f=d.playerResponse)||void 0===f?0:f.trackingParams)&&Ml(a.client,g,h,[xl(d.playerResponse.trackingParams)]))})}
function Lm(a,b,c,d){d=void 0===d?0:d;if(a.i.has(d))a.u.push([b,c]);else{var e=Dl(d);c=c||Bl(d);e&&c&&Ml(a.client,e,c,[b])}}
Jm.prototype.clickCommand=function(a,b,c){a=a.clickTrackingParams;c=void 0===c?0:c;if(a)if(c=Dl(void 0===c?0:c)){var d=this.client;var e="INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK";a={csn:c,ve:xl(a).getAsJson(),gestureType:e};b&&(a.clientData=b);b={cttAuthInfo:Fl(c),U:c};"UNDEFINED_CSN"==c?Nl("visualElementGestured",a,b):d?Kh("visualElementGestured",a,d,b):Fk("visualElementGestured",a,b);b=!0}else b=!1;else b=!1;return b};
function Mm(a,b,c){c=void 0===c?{}:c;a.i.add(c.layer||0);a.j=function(){Nm(a,b,c);var f=Bl(c.layer);if(f){for(var g=u(a.u),h=g.next();!h.done;h=g.next())h=h.value,Lm(a,h[0],h[1]||f,c.layer);f=u(a.o);for(g=f.next();!g.done;g=f.next()){var k=g.value;g=void 0;g=void 0===g?0:g;h=Dl(g);var l=k[0]||Bl(g);h&&l&&(g=a.client,k=k[1],k={csn:h,ve:l.getAsJson(),clientData:k},l={cttAuthInfo:Fl(h),U:h},"UNDEFINED_CSN"==h?Nl("visualElementStateChanged",k,l):g?Kh("visualElementStateChanged",k,g,l):Fk("visualElementStateChanged",
k,l))}}};
Dl(c.layer)||a.j();if(c.Ga)for(var d=u(c.Ga),e=d.next();!e.done;e=d.next())Km(a,e.value,c.layer);else Zk(Error("Delayed screen needs a data promise."))}
function Nm(a,b,c){c=void 0===c?{}:c;c.layer||(c.layer=0);var d=void 0!==c.jb?c.jb:c.layer;var e=Dl(d);d=Bl(d);var f;d&&(void 0!==c.parentCsn?f={clientScreenNonce:c.parentCsn,visualElement:d}:e&&"UNDEFINED_CSN"!==e&&(f={clientScreenNonce:e,visualElement:d}));var g,h=F("EVENT_ID");"UNDEFINED_CSN"===e&&h&&(g={servletData:{serializedServletEventId:h}});try{var k=a.client;h=f;var l=c.Fa,n=c.cttAuthInfo,q=Kl(),r={csn:q,pageVe:(new wl({veType:b,youtubeData:g})).getAsJson()};h&&h.visualElement?r.implicitGesture=
{parentCsn:h.clientScreenNonce,gesturedVe:h.visualElement.getAsJson()}:h&&Yk(new xi("newScreen() parent element does not have a VE - rootVe",b));l&&(r.cloneCsn=l);l={cttAuthInfo:n,U:q};k?Kh("screenCreated",r,k,l):Fk("screenCreated",r,l);ji(mi,new Hl(q));var p=q}catch(z){$k(z,{Sl:b,rootVe:d,parentVisualElement:void 0,Nl:e,Rl:f,Fa:c.Fa});Zk(z);return}Gl(p,b,c.layer,c.cttAuthInfo);if((b=e&&"UNDEFINED_CSN"!==e&&d)&&!(b=O("screen_manager_skip_hide_killswitch"))){a:{b=u(Object.values(vl));for(f=b.next();!f.done;f=
b.next())if(Dl(f.value)==e){b=!0;break a}b=!1}b=!b}b&&(b=a.client,f=!0,k=(f=void 0===f?!1:f)?16:8,d={csn:e,ve:d.getAsJson(),eventType:k},f={cttAuthInfo:Fl(e),U:e,Va:f},"UNDEFINED_CSN"==e?Nl("visualElementHidden",d,f):b?Kh("visualElementHidden",d,b,f):Fk("visualElementHidden",d,f));a.h[a.h.length-1]&&!a.h[a.h.length-1].csn&&(a.h[a.h.length-1].csn=p||"");Cm("csn",p);Ol.getInstance().clear();d=Bl(c.layer);e&&"UNDEFINED_CSN"!==e&&d&&(O("web_mark_root_visible")||O("music_web_mark_root_visible"))&&(e=p,
p={csn:e,ve:d.getAsJson(),eventType:1},b={cttAuthInfo:Fl(e),U:e},"UNDEFINED_CSN"==e?Nl("visualElementShown",p,b):Fk("visualElementShown",p,b));a.i.delete(c.layer||0);a.j=void 0;e=u(a.A);for(p=e.next();!p.done;p=e.next())b=u(p.value),p=b.next().value,b=b.next().value,b.has(c.layer)&&d&&Lm(a,p,d,c.layer);for(c=0;c<a.l.length;c++){e=a.l[c];try{e()}catch(z){Zk(z)}}for(c=a.l.length=0;c<a.m.length;c++){e=a.m[c];try{e()}catch(z){Zk(z)}}}
;function Om(a){a&&(a.dataset?a.dataset[Pm("loaded")]="true":a.setAttribute("data-loaded","true"))}
function Qm(a,b){return a?a.dataset?a.dataset[Pm(b)]:a.getAttribute("data-"+b):null}
var Rm={};function Pm(a){return Rm[a]||(Rm[a]=String(a).replace(/\-([a-z])/g,function(b,c){return c.toUpperCase()}))}
;var Sm=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,Tm=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function Um(a,b,c){c=void 0===c?null:c;if(window.spf&&spf.script){c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(Sm,""),c=c.replace(Tm,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else Vm(a,b,c)}
function Vm(a,b,c){c=void 0===c?null:c;var d=Wm(a),e=document.getElementById(d),f=e&&Qm(e,"loaded"),g=e&&!f;f?b&&b():(b&&(f=gh(d,b),b=""+Ka(b),Xm[b]=f),g||(e=Ym(a,d,function(){Qm(e,"loaded")||(Om(e),jh(d),cg(Qa(kh,d),0))},c)))}
function Ym(a,b,c,d){d=void 0===d?null:d;var e=Vc(document,"SCRIPT");e.id=b;e.onload=function(){c&&setTimeout(c,0)};
e.onreadystatechange=function(){switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);Oc(e,Me(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function Zm(a){a=Wm(a);var b=document.getElementById(a);b&&(kh(a),b.parentNode.removeChild(b))}
function $m(a,b){a&&b&&(a=""+Ka(b),(a=Xm[a])&&ih(a))}
function Wm(a){var b=document.createElement("a");Wb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+ac(a)}
var Xm={};var an=[],bn=!1;function cn(){if(!O("disable_biscotti_fetch_for_ad_blocker_detection")&&!O("disable_biscotti_fetch_entirely_for_all_web_clients")&&il()&&"1"!=ib()){var a=function(){bn=!0;"google_ad_status"in window?N("DCLKSTAT",1):N("DCLKSTAT",2)};
try{Um("//static.doubleclick.net/instream/ad_status.js",a)}catch(b){}an.push(ig(function(){if(!(bn||"google_ad_status"in window)){try{$m("//static.doubleclick.net/instream/ad_status.js",a)}catch(b){}bn=!0;N("DCLKSTAT",3)}},5E3))}}
function dn(){var a=Number(F("DCLKSTAT",0));return isNaN(a)?0:a}
;function en(){this.i=!1;this.h=null}
en.prototype.initialize=function(a,b,c,d){d=void 0===d?!1:d;var e,f;if(a.program){var g=null!==(e=a.interpreterScript)&&void 0!==e?e:null,h=null!==(f=a.interpreterUrl)&&void 0!==f?f:null;if(a.interpreterSafeScript){g=a.interpreterSafeScript;sb("From proto message. b/166824318");g=g.privateDoNotAccessOrElseSafeScriptWrappedValue||"";var k=pb();g=k?k.createScript(g):g;g=(new ub(g)).toString()}a.interpreterSafeUrl&&(h=a.interpreterSafeUrl,sb("From proto message. b/166824318"),h=yb(h.privateDoNotAccessOrElseTrustedResourceUrlWrappedValue||
"").toString());fn(this,g,h,a.program,b,c,d)}else Yk(Error("Cannot initialize botguard without program"))};
function fn(a,b,c,d,e,f,g){g=void 0===g?!1:g;c?(a.i=!0,Um(c,function(){a.i=!1;var h=0<=c.indexOf("/th/");(h?window.trayride:window.botguard)?gn(a,d,!!g,h,e):(Zm(c),Yk(new xi("Unable to load Botguard","from "+c)))},f)):b&&(f=Vc(document,"SCRIPT"),f.textContent=b,f.nonce=Zb(),document.head.appendChild(f),document.head.removeChild(f),((b=b.includes("trayride"))?window.trayride:window.botguard)?gn(a,d,!!g,b,e):Yk(Error("Unable to load Botguard from JS")))}
function gn(a,b,c,d,e){var f,g;if(d=d?null===(f=window.trayride)||void 0===f?void 0:f.ad:null===(g=window.botguard)||void 0===g?void 0:g.bg)if(c)try{hn(a,new d(b,e?function(){return e(b)}:Ea))}catch(h){h instanceof Error&&Yk(h)}else{try{hn(a,new d(b))}catch(h){h instanceof Error&&Yk(h)}e&&e(b)}else Yk(Error("Failed to finish initializing VM"))}
en.prototype.invoke=function(a){a=void 0===a?{}:a;return this.h?this.h.hasOwnProperty("hot")?this.h.hot(void 0,void 0,a):this.h.invoke(void 0,void 0,a):null};
en.prototype.dispose=function(){this.h=null};
function hn(a,b){a.h=b}
;var jn=new en;function kn(){return!!jn.h}
function ln(a){a=void 0===a?{}:a;return jn.invoke(a)}
;var mn=window,nn=/[A-Za-z]+\/[0-9.]+/g;function on(a,b){if(a.replace(nn,"")!==b.replace(nn,""))return!1;a=a.match(nn);b=b.match(nn);if(a.length!==b.length)return!1;for(var c=0;c<a.length;c++){var d=a[c],e=b[c];if(!d.startsWith(e)&&!e.startsWith(d))return!1}return!0}
function pn(){var a=mn.uaChPolyfill.state;if(0===a.type)Fk("clientHintsPolyfillEvent",{clientHintsSupported:!1});else{var b=navigator.userAgent,c=void 0!==a.syntheticUa&&on(a.syntheticUa,b),d={clientHintsSupported:!0,uaAccessedBeforePolyfill:a.didAccessUaBeforePolyfillAvailable,syntheticUaMatches:c};a.didAccessUaBeforePolyfillAvailable&&(d.uaAccessBeforePolyfillCount=a.uaAccessBeforePolyfillCount,a.firstAccessUaError&&(d.firstUaAccessStack=String(a.firstAccessUaError.stack).replace(/\n/g,""),Zk(a.firstAccessUaError)),
d.polyfillAvailabilityDelayMs=a.polyfillAvailabilityDelay);Fk("clientHintsPolyfillEvent",d);c||(b={syntheticUa:a.syntheticUa,ua:b},b.brand=a.data.brands.map(function(e){return'"'+e.brand+'"; v="'+e.version+'"'}),b.mobileness=a.data.mobile,a=a.data.values,a.architecture&&(b.platformArchitecture=a.architecture),a.model&&(b.model=a.model),a.platform&&(b.platformBrand=a.platform),a.platformVersion&&(b.platformVersion=a.platformVersion),a.uaFullVersion&&(b.fullVersion=a.uaFullVersion),Fk("clientHintsPolyfillDiagnostics",
b))}}
var qn=!1;function rn(){var a;1===(null===(a=mn.uaChPolyfill)||void 0===a?void 0:a.state.type)?qn||(mn.uaChPolyfill.onReady=rn,qn=!0):mn.uaChPolyfill&&pn()}
;function sn(a,b,c){L.call(this);var d=this;c=c||F("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname;this.j=b||null;this.C="*";this.l=c;this.sessionId=null;this.channel="widget";this.F=!!a;this.A=function(e){a:if(!("*"!=d.l&&e.origin!=d.l||d.j&&e.source!=d.j||"string"!==typeof e.data)){try{var f=JSON.parse(e.data)}catch(g){break a}if(!(null==f||d.F&&(d.sessionId&&d.sessionId!=f.id||d.channel&&d.channel!=f.channel))&&f)switch(f.event){case "listening":"null"!=
e.origin&&(d.l=d.C=e.origin);d.j=e.source;d.sessionId=f.id;d.i&&(d.i(),d.i=null);break;case "command":d.m&&(!d.o||0<=Wa(d.o,f.func))&&d.m(f.func,f.args,e.origin)}}};
this.o=this.i=this.m=null;window.addEventListener("message",this.A)}
v(sn,L);sn.prototype.sendMessage=function(a,b){if(b=b||this.j){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var c=JSON.stringify(a);b.postMessage(c,this.C)}catch(d){Nf(d)}}};
sn.prototype.D=function(){window.removeEventListener("message",this.A);L.prototype.D.call(this)};function tn(){this.i=[];this.isReady=!1;this.j={};var a=this.h=new sn(!!F("WIDGET_ID_ENFORCE")),b=this.lb.bind(this);a.m=b;a.o=null;this.h.channel="widget";if(a=F("WIDGET_ID"))this.h.sessionId=a}
m=tn.prototype;m.lb=function(a,b,c){"addEventListener"===a&&b?(a=b[0],this.j[a]||"onReady"===a||(this.addEventListener(a,un(this,a)),this.j[a]=!0)):this.Ba(a,b,c)};
m.Ba=function(){};
function un(a,b){return function(c){return a.sendMessage(b,c)}}
m.addEventListener=function(){};
m.Wa=function(){this.isReady=!0;this.sendMessage("initialDelivery",this.ta());this.sendMessage("onReady");D(this.i,this.Na,this);this.i=[]};
m.ta=function(){return null};
function vn(a,b){a.sendMessage("infoDelivery",b)}
m.Na=function(a){this.isReady?this.h.sendMessage(a):this.i.push(a)};
m.sendMessage=function(a,b){this.Na({event:a,info:void 0===b?null:b})};
m.dispose=function(){this.h=null};function wn(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function xn(a,b,c){if("string"===typeof a)return{videoId:a,startSeconds:b,suggestedQuality:c};b=["endSeconds","startSeconds","mediaContentUrl","suggestedQuality","videoId"];c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}
function yn(a,b,c,d){if(Ia(a)&&!Array.isArray(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};"string"===typeof a&&16===a.length?b.list="PL"+a:b.playlist=a;return b}
;function zn(a){tn.call(this);this.listeners=[];this.api=a;this.addEventListener("onReady",this.onReady.bind(this));this.addEventListener("onVideoProgress",this.sb.bind(this));this.addEventListener("onVolumeChange",this.tb.bind(this));this.addEventListener("onApiChange",this.nb.bind(this));this.addEventListener("onPlaybackQualityChange",this.pb.bind(this));this.addEventListener("onPlaybackRateChange",this.qb.bind(this));this.addEventListener("onStateChange",this.rb.bind(this));this.addEventListener("onWebglSettingsChanged",
this.ub.bind(this))}
v(zn,tn);m=zn.prototype;
m.Ba=function(a,b,c){if(this.api.isExternalMethodAvailable(a,c)){b=b||[];if(0<b.length&&wn(a)){var d=b;if(Ia(d[0])&&!Array.isArray(d[0]))var e=d[0];else switch(e={},a){case "loadVideoById":case "cueVideoById":e=xn(d[0],void 0!==d[1]?Number(d[1]):void 0,d[2]);break;case "loadVideoByUrl":case "cueVideoByUrl":e=d[0];"string"===typeof e&&(e={mediaContentUrl:e,startSeconds:void 0!==d[1]?Number(d[1]):void 0,suggestedQuality:d[2]});b:{if((d=e.mediaContentUrl)&&(d=/\/([ve]|embed)\/([^#?]+)/.exec(d))&&d[2]){d=
d[2];break b}d=null}e.videoId=d;e=xn(e);break;case "loadPlaylist":case "cuePlaylist":e=yn(d[0],d[1],d[2],d[3])}b.length=1;b[0]=e}this.api.handleExternalCall(a,b,c);wn(a)&&vn(this,this.ta())}};
m.onReady=function(){var a=this.Wa.bind(this);this.h.i=a};
m.addEventListener=function(a,b){this.listeners.push({eventType:a,listener:b});this.api.addEventListener(a,b)};
m.ta=function(){if(!this.api)return null;var a=this.api.getApiInterface();ab(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c];if(0===e.search("get")||0===e.search("is")){var f=0;0===e.search("get")?f=3:0===e.search("is")&&(f=2);f=e.charAt(f).toLowerCase()+e.substr(f+1);try{var g=this.api[e]();b[f]=g}catch(h){}}}b.videoData=this.api.getVideoData();b.currentTimeLastUpdated_=Date.now()/1E3;return b};
m.rb=function(a){a={playerState:a,currentTime:this.api.getCurrentTime(),duration:this.api.getDuration(),videoData:this.api.getVideoData(),videoStartBytes:0,videoBytesTotal:this.api.getVideoBytesTotal(),videoLoadedFraction:this.api.getVideoLoadedFraction(),playbackQuality:this.api.getPlaybackQuality(),availableQualityLevels:this.api.getAvailableQualityLevels(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getVideoUrl&&
(a.videoUrl=this.api.getVideoUrl());this.api.getVideoContentRect&&(a.videoContentRect=this.api.getVideoContentRect());this.api.getProgressState&&(a.progressState=this.api.getProgressState());this.api.getPlaylist&&(a.playlist=this.api.getPlaylist());this.api.getPlaylistIndex&&(a.playlistIndex=this.api.getPlaylistIndex());this.api.getStoryboardFormat&&(a.storyboardFormat=this.api.getStoryboardFormat());vn(this,a)};
m.pb=function(a){vn(this,{playbackQuality:a})};
m.qb=function(a){vn(this,{playbackRate:a})};
m.nb=function(){for(var a=this.api.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.api.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],l=this.api.getOption(e,k);b[e][k]=l}}this.sendMessage("apiInfoDelivery",b)};
m.tb=function(){vn(this,{muted:this.api.isMuted(),volume:this.api.getVolume()})};
m.sb=function(a){a={currentTime:a,videoBytesLoaded:this.api.getVideoBytesLoaded(),videoLoadedFraction:this.api.getVideoLoadedFraction(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getProgressState&&(a.progressState=this.api.getProgressState());vn(this,a)};
m.ub=function(){var a={sphericalProperties:this.api.getSphericalProperties()};vn(this,a)};
m.dispose=function(){tn.prototype.dispose.call(this);for(var a=0;a<this.listeners.length;a++){var b=this.listeners[a];this.api.removeEventListener(b.eventType,b.listener)}this.listeners=[]};function An(a){L.call(this);this.i={};this.started=!1;this.connection=a;this.connection.subscribe("command",this.Ma,this)}
v(An,L);m=An.prototype;m.start=function(){this.started||this.h||(this.started=!0,this.connection.X("RECEIVING"))};
m.X=function(a,b){this.started&&!this.h&&this.connection.X(a,b)};
m.Ma=function(a,b,c){if(this.started&&!this.h){var d=b||{};switch(a){case "addEventListener":"string"===typeof d.event&&this.addListener(d.event);break;case "removeEventListener":"string"===typeof d.event&&this.removeListener(d.event);break;default:this.api.isReady()&&this.api.isExternalMethodAvailable(a,c||null)&&(b=Bn(a,b||{}),c=this.api.handleExternalCall(a,b,c||null),(c=Cn(a,c))&&this.X(a,c))}}};
m.addListener=function(a){if(!(a in this.i)){var b=this.ob.bind(this,a);this.i[a]=b;this.addEventListener(a,b)}};
m.ob=function(a,b){this.started&&!this.h&&this.connection.X(a,this.sa(a,b))};
m.sa=function(a,b){if(null!=b)return{value:b}};
m.removeListener=function(a){a in this.i&&(this.removeEventListener(a,this.i[a]),delete this.i[a])};
m.D=function(){var a=this.connection;a.h||nf(a.i,"command",this.Ma,this);this.connection=null;for(var b in this.i)this.i.hasOwnProperty(b)&&this.removeListener(b);L.prototype.D.call(this)};function Dn(a,b){An.call(this,b);this.api=a;this.start()}
v(Dn,An);Dn.prototype.addEventListener=function(a,b){this.api.addEventListener(a,b)};
Dn.prototype.removeEventListener=function(a,b){this.api.removeEventListener(a,b)};
function Bn(a,b){switch(a){case "loadVideoById":return a=xn(b),[a];case "cueVideoById":return a=xn(b),[a];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return a=yn(b),[a];case "cuePlaylist":return a=yn(b),[a];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];
case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function Cn(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
Dn.prototype.sa=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return An.prototype.sa.call(this,a,b)};
Dn.prototype.D=function(){An.prototype.D.call(this);delete this.api};function En(a){a=void 0===a?!1:a;L.call(this);this.i=new M(a);Ud(this,Qa(Sd,this.i))}
C(En,L);En.prototype.subscribe=function(a,b,c){return this.h?0:this.i.subscribe(a,b,c)};
En.prototype.l=function(a,b){this.h||this.i.W.apply(this.i,arguments)};function Fn(a,b,c){En.call(this);this.j=a;this.destination=b;this.id=c}
v(Fn,En);Fn.prototype.X=function(a,b){this.h||this.j.X(this.destination,this.id,a,b)};
Fn.prototype.D=function(){this.destination=this.j=null;En.prototype.D.call(this)};function Gn(a,b,c){L.call(this);this.destination=a;this.origin=c;this.i=$f(window,"message",this.j.bind(this));this.connection=new Fn(this,a,b);Ud(this,Qa(Sd,this.connection))}
v(Gn,L);Gn.prototype.X=function(a,b,c,d){this.h||a!==this.destination||(a={id:b,command:c},d&&(a.data=d),this.destination.postMessage(Oe(a),this.origin))};
Gn.prototype.j=function(a){var b;if(b=!this.h)if(b=a.origin===this.origin)a:{b=this.destination;do{b:{var c=a.source;do{if(c===b){c=!0;break b}if(c===c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,"string"===typeof b)){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.connection,c.h||c.l("command",b.command,b.data,a.origin))}};
Gn.prototype.D=function(){ag(this.i);this.destination=null;L.prototype.D.call(this)};function Hn(){L.call(this);this.i=[]}
v(Hn,L);Hn.prototype.D=function(){for(;this.i.length;){var a=this.i.pop();a.target.removeEventListener(a.name,a.Da,void 0)}L.prototype.D.call(this)};function In(a){a=a||{};var b={},c={};this.url=a.url||"";this.args=a.args||kb(b);this.assets=a.assets||{};this.attrs=a.attrs||kb(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
In.prototype.clone=function(){var a=new In,b;for(b in this)if(this.hasOwnProperty(b)){var c=this[b];"object"==Ga(c)?a[b]=kb(c):a[b]=c}return a};var Jn=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function Kn(a){a=a||"";if(window.spf){var b=a.match(Jn);spf.style.load(a,b?b[1]:"",void 0)}else Ln(a)}
function Ln(a){var b=Mn(a),c=document.getElementById(b),d=c&&Qm(c,"loaded");d||c&&!d||(c=Nn(a,b,function(){Qm(c,"loaded")||(Om(c),jh(b),cg(Qa(kh,b),0))}))}
function Nn(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Me(a);Xb(d,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function Mn(a){var b=Vc(document,"A");sb("This URL is never added to the DOM");Wb(b,new Hb(a,Ib));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+ac(a)}
;function On(a,b,c,d){L.call(this);var e=this;this.F=b;this.webPlayerContextConfig=d;this.na=!1;this.api={};this.aa=this.m=null;this.I=new M;this.i={};this.N=this.ea=this.elementId=this.oa=this.config=null;this.M=!1;this.l=this.A=null;this.fa={};this.Oa=["onReady"];this.lastError=null;this.Ca=NaN;this.C={};this.Pa=new Hn(this);this.Z=0;this.j=this.o=a;Ud(this,Qa(Sd,this.I));Pn(this);Qn(this);Ud(this,Qa(Sd,this.Pa));c?this.Z=cg(function(){e.loadNewVideoConfig(c)},0):d&&(Rn(this),Sn(this))}
v(On,L);m=On.prototype;m.getId=function(){return this.F};
m.loadNewVideoConfig=function(a){if(!this.h){this.Z&&(dg(this.Z),this.Z=0);var b=a||{};b instanceof In||(b=new In(b));this.config=b;this.setConfig(a);Sn(this);this.isReady()&&Tn(this)}};
function Rn(a){var b,c;a.webPlayerContextConfig?c=a.webPlayerContextConfig.rootElementId:c=a.config.attrs.id;a.elementId=c||a.elementId;"video-player"===a.elementId&&(a.elementId=a.F,a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.F:a.config.attrs.id=a.F);(null===(b=a.j)||void 0===b?void 0:b.id)===a.elementId&&(a.elementId+="-player",a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.elementId:a.config.attrs.id=a.elementId)}
m.setConfig=function(a){var b;this.oa=a;this.config=Un(a);Rn(this);this.ea||(this.ea=Vn(this,(null===(b=this.config.args)||void 0===b?void 0:b.jsapicallback)||"onYouTubePlayerReady"));this.config.args?this.config.args.jsapicallback=null:this.config.args={jsapicallback:null};var c;if(null===(c=this.config)||void 0===c?0:c.attrs)a=this.config.attrs,(c=a.width)&&this.j&&(this.j.style.width=fd(Number(c)||c)),(a=a.height)&&this.j&&(this.j.style.height=fd(Number(a)||a))};
function Tn(a){var b;a.config&&!0!==a.config.loaded&&(a.config.loaded=!0,!a.config.args||"0"!==a.config.args.autoplay&&0!==a.config.args.autoplay&&!1!==a.config.args.autoplay?a.api.loadVideoByPlayerVars(null!==(b=a.config.args)&&void 0!==b?b:null):a.api.cueVideoByPlayerVars(a.config.args))}
function Wn(a){var b=!0,c=Xn(a);c&&a.config&&(a=Yn(a),b=Qm(c,"version")===a);return b&&!!B("yt.player.Application.create")}
function Sn(a){if(!a.h&&!a.M){var b=Wn(a);if(b&&"html5"===(Xn(a)?"html5":null))a.N="html5",a.isReady()||Zn(a);else if($n(a),a.N="html5",b&&a.l&&a.o)a.o.appendChild(a.l),Zn(a);else{a.config&&(a.config.loaded=!0);var c=!1;a.A=function(){c=!0;var d=ao(a,"player_bootstrap_method")?B("yt.player.Application.createAlternate")||B("yt.player.Application.create"):B("yt.player.Application.create");var e=a.config?Un(a.config):void 0;d&&d(a.o,e,a.webPlayerContextConfig);Zn(a)};
a.M=!0;b?a.A():(Um(Yn(a),a.A),(b=bo(a))&&Kn(b),co(a)&&!c&&A("yt.player.Application.create",null,void 0))}}}
function Xn(a){var b=Rc(a.elementId);!b&&a.j&&a.j.querySelector&&(b=a.j.querySelector("#"+a.elementId));return b}
function Zn(a){var b;if(!a.h){var c=Xn(a),d=!1;c&&c.getApiInterface&&c.getApiInterface()&&(d=!0);d?(a.M=!1,!ao(a,"html5_remove_not_servable_check_killswitch")&&(null===c||void 0===c?0:c.isNotServable)&&a.config&&(null===c||void 0===c?0:c.isNotServable(null===(b=a.config.args)||void 0===b?void 0:b.video_id))||eo(a)):a.Ca=cg(function(){Zn(a)},50)}}
function eo(a){Pn(a);a.na=!0;var b=Xn(a);if(b){a.m=fo(a,b,"addEventListener");a.aa=fo(a,b,"removeEventListener");var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=a.api,e=0;e<c.length;e++){var f=c[e];d[f]||(d[f]=fo(a,b,f))}}for(var g in a.i)a.i.hasOwnProperty(g)&&a.m&&a.m(g,a.i[g]);Tn(a);a.ea&&a.ea(a.api);a.I.W("onReady",a.api)}
function fo(a,b,c){var d=b[c];return function(e){for(var f=[],g=0;g<arguments.length;++g)f[g-0]=arguments[g];try{return a.lastError=null,d.apply(b,f)}catch(h){"sendAbandonmentPing"!==c&&(h.params=c,a.lastError=h,Yk(h))}}}
function Pn(a){a.na=!1;if(a.aa)for(var b in a.i)a.i.hasOwnProperty(b)&&a.aa(b,a.i[b]);for(var c in a.C)a.C.hasOwnProperty(c)&&dg(Number(c));a.C={};a.m=null;a.aa=null;b=a.api;for(var d in b)b.hasOwnProperty(d)&&(b[d]=null);b.addEventListener=function(e,f){a.addEventListener(e,f)};
b.removeEventListener=function(e,f){a.removeEventListener(e,f)};
b.destroy=function(){a.dispose()};
b.getLastError=function(){return a.getLastError()};
b.getPlayerType=function(){return a.getPlayerType()};
b.getCurrentVideoConfig=function(){return a.oa};
b.loadNewVideoConfig=function(e){a.loadNewVideoConfig(e)};
b.isReady=function(){return a.isReady()}}
m.isReady=function(){return this.na};
function Qn(a){a.addEventListener("WATCH_LATER_VIDEO_ADDED",function(b){jh("WATCH_LATER_VIDEO_ADDED",b)});
a.addEventListener("WATCH_LATER_VIDEO_REMOVED",function(b){jh("WATCH_LATER_VIDEO_REMOVED",b)});
a.addEventListener("onAdAnnounce",function(b){jh("a11y-announce",b)})}
m.addEventListener=function(a,b){var c=this,d=Vn(this,b);d&&(0<=Wa(this.Oa,a)||this.i[a]||(b=go(this,a),this.m&&this.m(a,b)),this.I.subscribe(a,d),"onReady"===a&&this.isReady()&&cg(function(){d(c.api)},0))};
m.removeEventListener=function(a,b){this.h||(b=Vn(this,b))&&nf(this.I,a,b)};
function Vn(a,b){var c=b;if("string"===typeof b){if(a.fa[b])return a.fa[b];c=function(d){for(var e=[],f=0;f<arguments.length;++f)e[f-0]=arguments[f];if(f=B(b))try{f.apply(y,e)}catch(g){Zk(g)}};
a.fa[b]=c}return c?c:null}
function go(a,b){var c="ytPlayer"+b+a.F;a.i[b]=c;y[c]=function(d){var e=cg(function(){if(!a.h){a.I.W(b,d);var f=a.C,g=String(e);g in f&&delete f[g]}},0);
hb(a.C,String(e))};
return c}
m.getPlayerType=function(){return this.N||(Xn(this)?"html5":null)};
m.getLastError=function(){return this.lastError};
function $n(a){a.cancel();Pn(a);a.N=null;a.config&&(a.config.loaded=!1);var b=Xn(a);b&&(Wn(a)||!co(a)?a.l=b:(b&&b.destroy&&b.destroy(),a.l=null));if(a.o)for(a=a.o;b=a.firstChild;)a.removeChild(b)}
m.cancel=function(){this.A&&$m(Yn(this),this.A);dg(this.Ca);this.M=!1};
m.D=function(){$n(this);if(this.l&&this.config&&this.l.destroy)try{this.l.destroy()}catch(b){Zk(b)}this.fa=null;for(var a in this.i)this.i.hasOwnProperty(a)&&(y[this.i[a]]=null);this.oa=this.config=this.api=null;delete this.o;delete this.j;L.prototype.D.call(this)};
function co(a){var b,c;a=null===(c=null===(b=a.config)||void 0===b?void 0:b.args)||void 0===c?void 0:c.fflags;return!!a&&-1!==a.indexOf("player_destroy_old_version=true")}
function Yn(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.jsUrl:(a=a.config.assets)?a.js:""}
function bo(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.cssUrl:(a=a.config.assets)?a.css:""}
function ao(a,b){var c;if(a.webPlayerContextConfig)var d=a.webPlayerContextConfig.serializedExperimentFlags;else if(null===(c=a.config)||void 0===c?0:c.args)d=a.config.args.fflags;return"true"===vg(d||"","&")[b]}
function Un(a){for(var b={},c=u(Object.keys(a)),d=c.next();!d.done;d=c.next()){d=d.value;var e=a[d];b[d]="object"===typeof e?kb(e):e}return b}
;var ho={},io="player_uid_"+(1E9*Math.random()>>>0);function jo(a,b,c){var d="player";c=void 0===c?!0:c;d="string"===typeof d?Rc(d):d;var e=io+"_"+Ka(d),f=ho[e];if(f&&c)return ko(a,b)?f.api.loadVideoByPlayerVars(a.args||null):f.loadNewVideoConfig(a),f.api;f=new On(d,e,a,b);ho[e]=f;jh("player-added",f.api);Ud(f,function(){delete ho[f.getId()]});
return f.api}
function ko(a,b){return b&&b.serializedExperimentFlags?b.serializedExperimentFlags.includes("web_player_remove_playerproxy=true"):a&&a.args&&a.args.fflags?a.args.fflags.includes("web_player_remove_playerproxy=true"):!1}
;var lo=null,mo=null,no=null;function oo(){var a=lo.getVideoData(1);a=a.title?a.title+" - YouTube":"YouTube";document.title!==a&&(document.title=a)}
;function po(a,b,c){a="ST-"+ac(a).toString(36);b=b?fc(b):"";c=c||5;il()&&Mh(a,b,c)}
;function qo(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=F("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=void 0===e?!0:e;var f=F("VALID_SESSION_TEMPDATA_DOMAINS",[]),g=dc(window.location.href);g&&f.push(g);g=dc(d);if(0<=Wa(f,g)||!g&&0==d.lastIndexOf("/",0))if(O("autoescape_tempdata_url")&&(f=document.createElement("a"),Wb(f,d),d=f.href),d){g=d.match(bc);d=g[5];f=g[6];g=g[7];var h="";d&&(h+=d);f&&(h+="?"+f);g&&(h+="#"+g);d=h;f=d.indexOf("#");if(d=0>f?d:d.substr(0,f))if(e&&!b.csn&&(b.itct||b.ved)&&
(b=Object.assign({csn:Dl()},b)),k){var k=parseInt(k,10);isFinite(k)&&0<k&&po(d,b,k)}else po(d,b)}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var l=void 0===l?{}:l;var n=void 0===n?"":n;var q=void 0===q?window:q;c=q.location;a=gc(a,l)+n;var r=void 0===r?ed:r;a:{r=void 0===r?ed:r;for(l=0;l<r.length;++l)if(n=r[l],n instanceof cd&&n.isValid(a)){r=new Lc(a,Jc);break a}r=void 0}c.href=Nc(r||Mc)}return!0}
;A("yt.setConfig",N,void 0);A("yt.config.set",N,void 0);A("yt.setMsg",Pf,void 0);A("yt.msgs.set",Pf,void 0);A("yt.logging.errors.log",Zk,void 0);
A("writeEmbed",function(){var a=F("PLAYER_CONFIG",void 0);if(!a){var b=F("PLAYER_VARS",void 0);b&&(a={args:b})}ql(!0);"gvn"===a.args.ps&&(document.body.style.backgroundColor="transparent");a.attrs||(a.attrs={width:"100%",height:"100%",id:"video-player"});var c=document.referrer;b=F("POST_MESSAGE_ORIGIN");window!==window.top&&c&&c!==document.URL&&(a.args.loaderUrl=c);O("embeds_js_api_set_1p_cookie")&&(c=Ag(),c.embedsTokenValue&&(a.args.embedsTokenValue=c.embedsTokenValue));N("FORCE_CSI_ON_GEL",!0);
c=["ol"];mm("").info.actionType="embed";c&&N("TIMING_AFT_KEYS",c);N("TIMING_ACTION","embed");c=F("TIMING_INFO",{});for(var d in c)c.hasOwnProperty(d)&&Cm(d,c[d]);Cm("is_nav",1);(d=Dl())&&Cm("csn",d);(d=F("PREVIOUS_ACTION",void 0))&&!xm()&&Cm("pa",d);d=hm();c=F("CLIENT_PROTOCOL");var e=F("CLIENT_TRANSPORT");c&&Cm("p",c);e&&Cm("t",e);Cm("yt_vis",Fm());Cm("yt_lt","cold");c=dm();if(e=fm())Z("srt",c.responseStart),1!==d.prerender&&(Cm("yt_sts","n",void 0),Z("_start",e,void 0));d=km();0<d&&Z("fpt",d);d=
dm();d.isPerformanceNavigationTiming&&Cm("pnt",1,void 0);Z("nreqs",d.requestStart,void 0);Z("nress",d.responseStart,void 0);Z("nrese",d.responseEnd,void 0);0<d.redirectEnd-d.redirectStart&&(Z("nrs",d.redirectStart,void 0),Z("nre",d.redirectEnd,void 0));0<d.domainLookupEnd-d.domainLookupStart&&(Z("ndnss",d.domainLookupStart,void 0),Z("ndnse",d.domainLookupEnd,void 0));0<d.connectEnd-d.connectStart&&(Z("ntcps",d.connectStart,void 0),Z("ntcpe",d.connectEnd,void 0));d.secureConnectionStart>=fm()&&0<d.connectEnd-
d.secureConnectionStart&&(Z("nstcps",d.secureConnectionStart,void 0),Z("ntcpe",d.connectEnd,void 0));W&&W.getEntriesByType&&Hm();d=[];if(document.querySelector&&W&&W.getEntriesByName)for(var f in am)am.hasOwnProperty(f)&&(c=am[f],Gm(f,c)&&d.push(c));for(f=0;f<d.length;f++)Cm("rc",d[f]);if(xm(void 0)){f={actionType:rm[F("TIMING_ACTION",void 0)]||"LATENCY_ACTION_UNKNOWN",previousAction:rm[F("PREVIOUS_ACTION",void 0)]||"LATENCY_ACTION_UNKNOWN"};if(d=Dl())f.clientScreenNonce=d;d=im(void 0);c=gm(void 0).cttAuthInfo;
pm().info(f,d,c)}f=hm();c=cm();if("cold"===f.yt_lt&&(d=zm(),e=d.gelTicks?d.gelTicks:d.gelTicks={},d=d.gelInfos?d.gelInfos:d.gelInfos={},xm())){for(var g in c)"tick_"+g in e||ym(g,c[g]);g=Bm();c=im();e=gm().cttAuthInfo;var h={},k=!1,l;for(l in f)if(!("info_"+l in d)){var n=Am(l,f[l]);n&&(Pl(g,n),Pl(h,n),k=!0)}k&&pm().info(h,c,e)}A("ytglobal.timingready_",!0,void 0);Dm();(l=F("WEB_PLAYER_CONTEXT_CONFIGS",void 0))&&"WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER"in l?(l=l.WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER,
l.serializedForcedExperimentIds||(g=Ag(),g.forced_experiments&&(l.serializedForcedExperimentIds=g.forced_experiments)),lo=jo(a,l,!1)):lo=jo(a);lo.addEventListener("onVideoDataChange",oo);a=F("POST_MESSAGE_ID","player");F("ENABLE_JS_API")?no=new zn(lo):F("ENABLE_POST_API")&&"string"===typeof a&&"string"===typeof b&&(mo=new Gn(window.parent,a,b),no=new Dn(lo,mo.connection));cn();O("networkless_logging_web_embedded")&&qk();O("embeds_enable_ua_ch_polyfill")&&rn()},void 0);
var ro=Lf(function(){Em();var a=Oh.getInstance(),b=!!((Rh("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&Xd(document.body,"exp-invert-logo"))if(c&&!Xd(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!Xd(d,"inverted-hdpi")){var e=Vd(d);Wd(d,e+(0<e.length?" inverted-hdpi":"inverted-hdpi"))}}else!c&&Xd(document.body,"inverted-hdpi")&&Yd();if(b!=c){b="f"+(Math.floor(119/31)+1);d=Rh(b)||0;d=c?d|67108864:
d&-67108865;0==d?delete Nh[b]:(c=d.toString(16),Nh[b]=c.toString());c=!0;O("web_secure_pref_cookie_killswitch")&&(c=!1);b=a.h;d=[];for(var f in Nh)d.push(f+"="+encodeURIComponent(String(Nh[f])));Mh(b,d.join("&"),63072E3,a.i,c)}Jm.h||(Jm.h=new Jm);a=Jm.h;f=16623;var g=void 0===g?{}:g;Object.values(al).includes(f)||(Yk(new xi("createClientScreen() called with a non-page VE",f)),f=83769);g.isHistoryNavigation||a.h.push({rootVe:f,key:g.key||""});a.u=[];a.o=[];g.Ga?Mm(a,f,g):Nm(a,f,g)}),so=Lf(function(){lo&&
lo.sendAbandonmentPing&&lo.sendAbandonmentPing();
F("PL_ATT")&&jn.dispose();for(var a=0,b=an.length;a<b;a++)kg(an[a]);an.length=0;Zm("//static.doubleclick.net/instream/ad_status.js");bn=!1;N("DCLKSTAT",0);Td(no,mo);lo&&(lo.removeEventListener("onVideoDataChange",oo),lo.destroy())});
window.addEventListener?(window.addEventListener("load",ro),window.addEventListener("unload",so)):window.attachEvent&&(window.attachEvent("onload",ro),window.attachEvent("onunload",so));Ra("yt.abuse.player.botguardInitialized",B("yt.abuse.player.botguardInitialized")||kn);Ra("yt.abuse.player.invokeBotguard",B("yt.abuse.player.invokeBotguard")||ln);Ra("yt.abuse.dclkstatus.checkDclkStatus",B("yt.abuse.dclkstatus.checkDclkStatus")||dn);
Ra("yt.player.exports.navigate",B("yt.player.exports.navigate")||qo);Ra("yt.util.activity.init",B("yt.util.activity.init")||mg);Ra("yt.util.activity.getTimeSinceActive",B("yt.util.activity.getTimeSinceActive")||pg);Ra("yt.util.activity.setTimestamp",B("yt.util.activity.setTimestamp")||ng);}).call(this);
