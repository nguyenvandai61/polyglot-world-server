(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4ce4847a"],{"02a2":function(t,e,s){"use strict";s("0acf")},"0acf":function(t,e,s){},"0c95":function(t,e,s){"use strict";s.r(e);var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"page-chat"},[s("div",{staticClass:"chat-header"},[s("div",{staticClass:"chat-header-title"},[s("h3",[t._v(t._s(t.title))])])]),s("list-chat")],1)},o=[],n=s("2b0e"),i=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"list-chat"},[s("v-row",[s("v-col",t._l(t.rooms,(function(t,e){return s("v-list-item",{key:e,class:{active:t.active}},[s("row-room",{attrs:{room:t}})],1)})),1),s("v-col",{attrs:{cols:"8"}},[s("chat-box",{attrs:{room:t.selected_room,messages:t.messages}})],1)],1)],1)},r=[],c=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("v-card",{staticClass:"row-room"},[s("v-row",{staticStyle:{"min-width":"300px"}},[s("v-col",{attrs:{cols:"12",sm:"4"}},[s("div",{staticClass:"col row-room__room-avatar"},[s("room-avatar",{attrs:{room_avatars:t.room.room_avatars}})],1)]),s("v-col",{attrs:{cols:"10",sm:"8"}},[s("div",{staticClass:"row-room__room-info"},[s("div",{staticClass:"row-room__room-title"},[t._v(" "+t._s(t.room.title)+" ")]),s("div",{staticClass:"row-room__room-description"},[s("div",{staticClass:"row-room__last-message"},[s("div",{staticClass:"row-room__last-message__content"},[s("p",[t._v(t._s(t.getLastMessage))])]),s("div",{staticClass:"row-room__last-message__time"},[s("p",[t._v(t._s(t.last_message_created_at))])]),s("div",{staticClass:"col row-room__room-status"})])])])])],1)],1)},m=[],l=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"room-avatar"},[t.room_avatars&&1==t.room_avatars.length?s("div",{staticClass:"room-avatar__one-user"},[s("v-avatar",{staticClass:"first-avatar"},[s("img",{attrs:{src:t.room_avatars[0],alt:"avatar_0"}})])],1):s("div",{staticClass:"room-avatar__two-user"},[s("v-avatar",{staticClass:"first-avatar",attrs:{size:"40px"}},[s("img",{attrs:{src:t.room_avatars[0],alt:"avatar_0"}})]),s("v-avatar",{staticClass:"second-avatar",attrs:{size:"40px"}},[s("img",{attrs:{src:t.room_avatars[1],alt:"avatar_1"}})])],1)])},_=[],u=n["default"].extend({name:"RoomAvatar",props:{room_avatars:{type:Array,required:!0,default:function(){return[]}}},data:function(){return{}}}),d=u,v=(s("91e4"),s("2877")),p=Object(v["a"])(d,l,_,!1,null,"f3f0488c",null),g=p.exports,f=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"room-status"},[t.is_notified?"unseen"===t.status?s("div",{staticClass:"room-status__icon"},[s("v-icon",[t._v(" mdi-checkbox-marked-circle ")])],1):"seen"===t.status?s("div",{staticClass:"room-status__icon"},[s("v-avatar",{attrs:{size:"20px"}},[s("img",{attrs:{src:t.seen_user_avatar,alt:""}})])],1):t._e():s("div",{staticClass:"room-status__icon"},[s("v-icon",[t._v(" mdi-bell-off ")])],1)])},h=[],b=n["default"].extend({name:"RoomStatus",props:{status:{type:String},seen_user_avatar:{type:String},is_notified:{type:Boolean}}}),x=b,C=Object(v["a"])(x,f,h,!1,null,null,null),w=(C.exports,n["default"].extend({name:"RowRoom",components:{RoomAvatar:g},data:function(){return{}},props:{room:{type:Object,required:!0,default:function(){return{id:0,title:"",room_avatars:[],user_avatars:[],last_message:"",last_message_status:"",last_message_created_at:"",is_notified:!1}}}},computed:{user_avatars:function(){return this.room.user_avatars},getLastMessage:function(){return this.room.last_message?this.room.last_message.sender.first_name+": "+this.room.last_message.message:""},last_message_created_at:function(){return this.room.last_message?this.room.last_message.created_at:""},last_message_status:function(){return this.room.last_message?this.room.last_message.status:""}}})),y=w,k=(s("02a2"),Object(v["a"])(y,c,m,!1,null,"411fd0ae",null)),E=k.exports,L=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{attrs:{id:"chat-box"}},[s("v-container",[s("div",{staticClass:"chat-box__body"},[s("div",{staticClass:"chat-box__body__header mb-3"},[s("div",{staticClass:"chat-box__body__header__title"},[s("room-avatar",{attrs:{room_avatars:t.room_avatars}}),s("h4",[t._v(t._s(t.title))])],1)]),t._l(t.messages,(function(e){return s("v-row",{key:e.id,staticClass:"chat-box__body__message mb-3"},[s("message-box",{class:"chat-box__body__messages__message-box "+(e.is_guest?"guest":""),attrs:{name:e.name,is_guest:e.is_guest,avatar:t.user.avatar,content:e.content,reaction_emotions:e.reaction_emotions}})],1)})),s("v-row",{staticClass:"chat-box__body__input"},[s("div",{staticClass:"chat-box__body__input__text-field"},[s("v-text-field",{attrs:{label:"",autofocus:"",placeholder:"Type your message"},on:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.sendMessage.apply(null,arguments)}},model:{value:t.messageInput,callback:function(e){t.messageInput=e},expression:"messageInput"}})],1),s("div",{staticClass:"chat-box__body__input__send"},[s("v-btn",{on:{click:t.sendMessage}},[t._v("Send")])],1)])],2)])],1)},j=[],R=(s("b0c0"),function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"message-box"},[s("div",{class:"message-box__content "+(t.is_guest?"guest":"")},[t.is_guest?s("div",{staticClass:"message-box__content__user"},[s("v-avatar",{attrs:{size:"40"}},[s("img",{attrs:{src:t.avatar,alt:""}})])],1):t._e(),s("div",{staticClass:"message-box__content__right"},[t.is_guest?s("div",{staticClass:"message-box__content__name"},[s("span",[t._v(t._s(t.name))])]):t._e(),s("v-card",{directives:[{name:"longpress",rawName:"v-longpress",value:t.handleLongPress,expression:"handleLongPress"},{name:"longpress-stop",rawName:"v-longpress-stop",value:t.handleLongPressStop,expression:"handleLongPressStop"}],staticClass:"message-box__content__message"},[s("span",[t._v(t._s(t.content))]),s("reaction-emotion",{attrs:{emotions:t.reaction_emotions,emotion_picked:{id:1}}})],1),s("reaction-emotion-picker",{directives:[{name:"show",rawName:"v-show",value:t.is_show_emotion_picker,expression:"is_show_emotion_picker"}],attrs:{emotion_picked:{}},on:{"emotion-picked-off":t.handleLongPressStop}})],1)]),s("div",{staticClass:"message-box__time"},[s("span",[t._v(t._s(t.time))])])])}),S=[],O=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"reaction-emotion"},[s("div",{staticClass:"reaction-emotion__emotions"},t._l(t.emotions,(function(e){return s("div",{key:e.id,staticClass:"reaction-emotion__emotion"},[s("img",{attrs:{src:e.icon,alt:""}}),s("div",{directives:[{name:"show",rawName:"v-show",value:e.count>1,expression:"emotion.count > 1"}],staticClass:"reaction-emotion__count"},[t._v(" "+t._s(e.count)+" ")])])})),0)])},$=[],J=n["default"].extend({props:{},data:function(){return{emotions:[{id:1,icon:"https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png",count:1},{id:2,icon:"https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png",count:2}]}}}),P=J,T=(s("f7ae"),Object(v["a"])(P,O,$,!1,null,"32c99f76",null)),D=T.exports,I=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"reaction-emotion-picker"},[s("v-card",{staticClass:"reaction-emotion-picker__icons"},t._l(t.emotions,(function(e,a){return s("div",{key:e.id,staticClass:"reaction-emotion-picker__icon",on:{click:function(){return t.emotionClicked(a)}}},[s("img",{attrs:{src:e.icon,alt:e.name}}),t.emotion_picked.id==e.id?s("span",{staticClass:"dot"}):t._e()])})),0)],1)},M=[],z=(s("a9e3"),n["default"].extend({name:"ReactionEmotionPicker",props:{emotion_picked:{id:Number}},data:function(){return{emotions:[{id:1,icon:"https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png"},{id:2,icon:"https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png"},{id:3,icon:"https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png"}]}},methods:{emotionClicked:function(t){this.emotion_picked=this.emotions[t],this.$emit("emotion-picked-off",this.emotion_picked)}}})),B=z,H=(s("e24d"),Object(v["a"])(B,I,M,!1,null,"7fa75250",null)),N=H.exports;n["default"].directive("longpress",{bind:function(t,e,s){var a,o=function(){"function"===typeof e.value?e.value&&e.value(s.context):console.error("longpress binding value must be a function")};t.addEventListener("mousedown",(function(){a=setTimeout(o,500)})),t.addEventListener("mouseleave",(function(){clearTimeout(a)})),t.addEventListener("mouseup",(function(){clearTimeout(a)})),t.addEventListener("touchstart",(function(){a=setTimeout(o,500)})),t.addEventListener("touchend",(function(){clearTimeout(a)})),t.addEventListener("touchcancel",(function(){clearTimeout(a)}))}}),n["default"].directive("longpress-stop",{bind:function(t,e,s){var a=function(){"function"===typeof e.value?e.value&&e.value(s.context):console.error("longpress-stop binding value must be a function")};t.addEventListener("mouseleave",a),t.addEventListener("touchcancel",a)}});var q=n["default"].extend({name:"MessageBox",props:{is_guest:{type:Boolean},name:{type:String},avatar:{type:String},content:{},time:{type:String},reaction_emotions:{type:Object}},components:{ReactionEmotion:D,ReactionEmotionPicker:N},data:function(){return{is_show_emotion_picker:!1}},methods:{handleLongPress:function(){this.is_show_emotion_picker=!0},handleLongPressStop:function(){this.is_show_emotion_picker=!1}}}),A=q,U=(s("568a"),Object(v["a"])(A,R,S,!1,null,"f306a256",null)),Y=U.exports,Q=n["default"].extend({name:"ChatBox",components:{MessageBox:Y,RoomAvatar:g},props:{},data:function(){return{title:"Room 1",messageInput:"",room_avatars:["https://i.imgur.com/2Y9zqQY.png"],user:{name:"",avatar:"https://i.imgur.com/2Y9zqQY.png"},messages:[{id:1,name:"John Doe",is_guest:!1,content:"Hello, how are you?",reaction_emotions:{}},{id:2,name:"John Doe",is_guest:!0,content:"Hello, how are you?",reaction_emotions:{}},{id:3,name:"John Doe",is_guest:!1,content:"Hello, how are you?",reaction_emotions:{}},{id:4,name:"John Doe",is_guest:!1,content:"Hello, how are you?",reaction_emotions:{}},{id:5,name:"John Doe",is_guest:!1,content:"Hello, how are you?",reaction_emotions:{}}]}},methods:{sendMessage:function(){this.messageInput.length>0&&(this.messages.push({id:this.messages.length+1,name:this.user.name,content:this.messageInput}),this.messageInput="")}}}),F=Q,G=(s("d5db"),Object(v["a"])(F,L,j,!1,null,"7f07305d",null)),K=G.exports,V=n["default"].extend({name:"ListChat",components:{RowRoom:E,ChatBox:K},data:function(){return{selected_room:{id:0,name:"",active:!1},messages:[{id:0,user:"",message:"",date:""}],rooms:[{id:1,title:"Room 1",active:!0,room_avatars:["https://cdn.vuetifyjs.com/images/lists/2.jpg","https://cdn.vuetifyjs.com/images/lists/3.jpg"],last_message:{sender:{first_name:"John",last_name:"Doe"},message:"Hello",created_at:"2020-01-01"},users:[{id:1,name:"User 1"},{id:2,name:"User 2"}]},{id:2,title:"Room 2",active:!0,room_avatars:["https://cdn.vuetifyjs.com/images/lists/3.jpg"],users:[{id:1,name:"User 1"},{id:2,name:"User 2"}],last_message:{sender:{first_name:"John",last_name:"Doe"},message:"See you later",created_at:"2020-01-01"}}]}}}),W=V,X=Object(v["a"])(W,i,r,!1,null,null,null),Z=X.exports,tt=n["default"].extend({components:{ListChat:Z},data:function(){return{title:"Chat",list:[],searchText:"",text:""}},methods:{}}),et=tt,st=Object(v["a"])(et,a,o,!1,null,null,null);e["default"]=st.exports},"336f":function(t,e,s){},"568a":function(t,e,s){"use strict";s("ff46")},6394:function(t,e,s){},"91ca":function(t,e,s){},"91e4":function(t,e,s){"use strict";s("d1db")},d1db:function(t,e,s){},d5db:function(t,e,s){"use strict";s("6394")},e24d:function(t,e,s){"use strict";s("91ca")},f7ae:function(t,e,s){"use strict";s("336f")},ff46:function(t,e,s){}}]);