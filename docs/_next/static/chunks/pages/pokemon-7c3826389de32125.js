(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[673],{7658:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/pokemon",function(){return n(1533)}])},1533:function(e,t,n){"use strict";n.r(t),n.d(t,{Div_ac2a89ea84667d600a059f034bd91dfe:function(){return Div_ac2a89ea84667d600a059f034bd91dfe},Fragment_cf53a535ae2e610a113dd361eb6ac95b:function(){return Fragment_cf53a535ae2e610a113dd361eb6ac95b},Toaster_6e90e5e87a1cac8c96c683214079bef3:function(){return Toaster_6e90e5e87a1cac8c96c683214079bef3},default:function(){return Component}});var a=n(2729),r=n(1965),c=n(7294),o=n(687),i=n(6608),s=n(9894),l=n(917),d=n(4712),u=n(3954),m=n(3729),f=n(5893);function Hello(){let[e,t]=(0,c.useState)([{name:"",order:"",sprites:""}]),[n,a]=(0,c.useState)(0);async function getData(){try{let e=await fetch("https://pokeapi.co/api/v2/pokemon?limit=25&offset=".concat(n)),a=await e.json(),r=/\/(\d+)\//;t(a.results.map(e=>({name:e.name,order:e.url.match(r)[1],sprites:e.url.match(r)[1]})))}catch(e){console.error(e)}}return(0,c.useEffect)(()=>{getData()},[]),(0,f.jsxs)("div",{className:"w-full h-fit p-6",children:[(0,f.jsxs)("h1",{className:"text-center text-2xl font-bold",children:["Listado de Pokemones Inicio Actual: ",n]}),(0,f.jsxs)("div",{className:"w-full flex justify-between mb-2",children:[(0,f.jsx)("button",{className:"inline-block rounded border border-indigo-600 bg-indigo-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-indigo-600 focus:outline-none focus:ring active:text-indigo-500",onClick:()=>{n>=0&&(a(n-1),getData())},children:"Atras"}),(0,f.jsx)("button",{onClick:()=>{a(n+1),getData()},className:"inline-block rounded border border-indigo-600 bg-indigo-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-indigo-600 focus:outline-none focus:ring active:text-indigo-500",children:"Siguiente"})]}),(0,f.jsx)("div",{className:"w-full h-screen  overflow-scroll",children:(0,f.jsx)("div",{className:"mt-6 grid grid-cols-6 gap-4",children:e.map((e,t)=>(0,f.jsxs)("article",{className:"flex flex-col gap-4 rounded-lg border border-gray-100 bg-white p-6",children:[(0,f.jsxs)("span",{className:"text-2xl font-medium text-gray-900",children:["#",e.order]}),(0,f.jsx)("div",{className:"inline-flex gap-2 self-end rounded bg-green-100 p-1 text-green-600",children:(0,f.jsx)("img",{src:"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/".concat(e.sprites,".png"),alt:"imagen de un pokemon"})}),(0,f.jsx)("div",{children:(0,f.jsxs)("strong",{className:"block text-sm font-medium text-gray-500",children:[" Nombre: ",e.name," "]})})]},t))})})]})}var g=n(9008),h=n.n(g);function _templateObject(){let e=(0,a._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}function Fragment_cf53a535ae2e610a113dd361eb6ac95b(){let[e,t]=(0,c.useContext)(o.DR);return(0,r.tZ)(c.Fragment,{children:(0,i.oA)(t.length>0)?(0,r.tZ)(c.Fragment,{children:(0,r.tZ)(s.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:"".concat(p," 1s infinite")},size:32})}):(0,r.tZ)(c.Fragment,{})})}function Div_ac2a89ea84667d600a059f034bd91dfe(){let[e,t]=(0,c.useContext)(o.DR);return(0,r.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: ".concat(t.length>0?t[t.length-1].message:""),children:(0,r.tZ)(Fragment_cf53a535ae2e610a113dd361eb6ac95b,{})})}let p=(0,l.F4)(_templateObject());function Toaster_6e90e5e87a1cac8c96c683214079bef3(){let{resolvedColorMode:e}=(0,c.useContext)(o.kc);i.xL.__toast=d.A;let[t,n]=(0,c.useContext)(o.DR),a={description:"Check if server is reachable at ".concat((0,i.LH)(u.Ks).href),closeButton:!0,duration:12e4,id:"websocket-error"},[s,l]=(0,c.useState)(!1);return(0,c.useEffect)(()=>{n.length>=2?s||d.A.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...a,onDismiss:()=>l(!0)}):(d.A.dismiss("websocket-error"),l(!1))},[n]),(0,r.tZ)(d.x,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function Component(){return(0,r.BX)(c.Fragment,{children:[(0,r.BX)(c.Fragment,{children:[(0,r.tZ)(Div_ac2a89ea84667d600a059f034bd91dfe,{}),(0,r.tZ)(Toaster_6e90e5e87a1cac8c96c683214079bef3,{})]}),(0,r.tZ)(m.xu,{className:"w-full bg-green-300",children:(0,r.tZ)(m.kC,{css:{display:"flex",alignItems:"center",justifyContent:"center"},children:(0,r.BX)(m.kC,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,r.tZ)(m.xu,{className:"w-full",children:(0,r.tZ)(m.X6,{className:"text-center mt-6",children:"Reflex con React js"})}),(0,r.tZ)(Hello,{})]})})}),(0,r.BX)(h(),{children:[(0,r.tZ)("title",{children:"Apps"}),(0,r.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}}},function(e){e.O(0,[534,774,888,179],function(){return e(e.s=7658)}),_N_E=e.O()}]);