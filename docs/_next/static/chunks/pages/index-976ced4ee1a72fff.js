(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[405],{5557:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/",function(){return n(1250)}])},7498:function(e,t){"use strict";var n,r;Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var n in t)Object.defineProperty(e,n,{enumerable:!0,get:t[n]})}(t,{PrefetchKind:function(){return n},ACTION_REFRESH:function(){return o},ACTION_NAVIGATE:function(){return c},ACTION_RESTORE:function(){return a},ACTION_SERVER_PATCH:function(){return i},ACTION_PREFETCH:function(){return l},ACTION_FAST_REFRESH:function(){return u},ACTION_SERVER_ACTION:function(){return f}});let o="refresh",c="navigate",a="restore",i="server-patch",l="prefetch",u="fast-refresh",f="server-action";(r=n||(n={})).AUTO="auto",r.FULL="full",r.TEMPORARY="temporary",("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},30:function(e,t,n){"use strict";function getDomainLocale(e,t,n,r){return!1}Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"getDomainLocale",{enumerable:!0,get:function(){return getDomainLocale}}),n(2866),("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},5170:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return m}});let r=n(8754),o=r._(n(7294)),c=n(4450),a=n(2227),i=n(4364),l=n(109),u=n(3607),f=n(1823),s=n(9031),d=n(920),p=n(30),h=n(7192),b=n(7498),g=new Set;function prefetch(e,t,n,r,o,c){if(!c&&!(0,a.isLocalURL)(t))return;if(!r.bypassPrefetchedCheck){let o=void 0!==r.locale?r.locale:"locale"in e?e.locale:void 0,c=t+"%"+n+"%"+o;if(g.has(c))return;g.add(c)}let i=c?e.prefetch(t,o):e.prefetch(t,n,r);Promise.resolve(i).catch(e=>{})}function isModifiedEvent(e){let t=e.currentTarget,n=t.getAttribute("target");return n&&"_self"!==n||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.nativeEvent&&2===e.nativeEvent.which}function linkClicked(e,t,n,r,c,i,l,u,f,s){let{nodeName:d}=e.currentTarget,p="A"===d.toUpperCase();if(p&&(isModifiedEvent(e)||!f&&!(0,a.isLocalURL)(n)))return;e.preventDefault();let navigate=()=>{let e=null==l||l;"beforePopState"in t?t[c?"replace":"push"](n,r,{shallow:i,locale:u,scroll:e}):t[c?"replace":"push"](r||n,{forceOptimisticNavigation:!s,scroll:e})};f?o.default.startTransition(navigate):navigate()}function formatStringOrUrl(e){return"string"==typeof e?e:(0,i.formatUrl)(e)}let H=o.default.forwardRef(function(e,t){let n,r;let{href:a,as:i,children:g,prefetch:H=null,passHref:m,replace:_,shallow:v,scroll:V,locale:y,onClick:Z,onMouseEnter:k,onTouchStart:C,legacyBehavior:M=!1,...x}=e;n=g,M&&("string"==typeof n||"number"==typeof n)&&(n=o.default.createElement("a",null,n));let O=o.default.useContext(f.RouterContext),w=o.default.useContext(s.AppRouterContext),F=null!=O?O:w,E=!O,T=!1!==H,j=null===H?b.PrefetchKind.AUTO:b.PrefetchKind.FULL,{href:A,as:I}=o.default.useMemo(()=>{if(!O){let e=formatStringOrUrl(a);return{href:e,as:i?formatStringOrUrl(i):e}}let[e,t]=(0,c.resolveHref)(O,a,!0);return{href:e,as:i?(0,c.resolveHref)(O,i):t||e}},[O,a,i]),L=o.default.useRef(A),P=o.default.useRef(I);M&&(r=o.default.Children.only(n));let R=M?r&&"object"==typeof r&&r.ref:t,[S,N,D]=(0,d.useIntersection)({rootMargin:"200px"}),U=o.default.useCallback(e=>{(P.current!==I||L.current!==A)&&(D(),P.current=I,L.current=A),S(e),R&&("function"==typeof R?R(e):"object"==typeof R&&(R.current=e))},[I,R,A,D,S]);o.default.useEffect(()=>{F&&N&&T&&prefetch(F,A,I,{locale:y},{kind:j},E)},[I,A,N,y,T,null==O?void 0:O.locale,F,E,j]);let B={ref:U,onClick(e){M||"function"!=typeof Z||Z(e),M&&r.props&&"function"==typeof r.props.onClick&&r.props.onClick(e),F&&!e.defaultPrevented&&linkClicked(e,F,A,I,_,v,V,y,E,T)},onMouseEnter(e){M||"function"!=typeof k||k(e),M&&r.props&&"function"==typeof r.props.onMouseEnter&&r.props.onMouseEnter(e),F&&(T||!E)&&prefetch(F,A,I,{locale:y,priority:!0,bypassPrefetchedCheck:!0},{kind:j},E)},onTouchStart(e){M||"function"!=typeof C||C(e),M&&r.props&&"function"==typeof r.props.onTouchStart&&r.props.onTouchStart(e),F&&(T||!E)&&prefetch(F,A,I,{locale:y,priority:!0,bypassPrefetchedCheck:!0},{kind:j},E)}};if((0,l.isAbsoluteUrl)(I))B.href=I;else if(!M||m||"a"===r.type&&!("href"in r.props)){let e=void 0!==y?y:null==O?void 0:O.locale,t=(null==O?void 0:O.isLocaleDomain)&&(0,p.getDomainLocale)(I,e,null==O?void 0:O.locales,null==O?void 0:O.domainLocales);B.href=t||(0,h.addBasePath)((0,u.addLocale)(I,e,null==O?void 0:O.defaultLocale))}return M?o.default.cloneElement(r,B):o.default.createElement("a",{...x,...B},n)}),m=H;("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},920:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"useIntersection",{enumerable:!0,get:function(){return useIntersection}});let r=n(7294),o=n(3436),c="function"==typeof IntersectionObserver,a=new Map,i=[];function createObserver(e){let t;let n={root:e.root||null,margin:e.rootMargin||""},r=i.find(e=>e.root===n.root&&e.margin===n.margin);if(r&&(t=a.get(r)))return t;let o=new Map,c=new IntersectionObserver(e=>{e.forEach(e=>{let t=o.get(e.target),n=e.isIntersecting||e.intersectionRatio>0;t&&n&&t(n)})},e);return t={id:n,observer:c,elements:o},i.push(n),a.set(n,t),t}function observe(e,t,n){let{id:r,observer:o,elements:c}=createObserver(n);return c.set(e,t),o.observe(e),function(){if(c.delete(e),o.unobserve(e),0===c.size){o.disconnect(),a.delete(r);let e=i.findIndex(e=>e.root===r.root&&e.margin===r.margin);e>-1&&i.splice(e,1)}}}function useIntersection(e){let{rootRef:t,rootMargin:n,disabled:a}=e,i=a||!c,[l,u]=(0,r.useState)(!1),f=(0,r.useRef)(null),s=(0,r.useCallback)(e=>{f.current=e},[]);(0,r.useEffect)(()=>{if(c){if(i||l)return;let e=f.current;if(e&&e.tagName){let r=observe(e,e=>e&&u(e),{root:null==t?void 0:t.current,rootMargin:n});return r}}else if(!l){let e=(0,o.requestIdleCallback)(()=>u(!0));return()=>(0,o.cancelIdleCallback)(e)}},[i,n,t,l,f.current]);let d=(0,r.useCallback)(()=>{u(!1)},[]);return[s,l,d]}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},1250:function(e,t,n){"use strict";n.r(t),n.d(t,{Div_ac2a89ea84667d600a059f034bd91dfe:function(){return Div_ac2a89ea84667d600a059f034bd91dfe},Fragment_2e0e6a4a3aec4136eedf42fc142b7aae:function(){return Fragment_2e0e6a4a3aec4136eedf42fc142b7aae},Fragment_cf53a535ae2e610a113dd361eb6ac95b:function(){return Fragment_cf53a535ae2e610a113dd361eb6ac95b},Iconbutton_126c1207e75571062288a84458b7ab68:function(){return Iconbutton_126c1207e75571062288a84458b7ab68},Link_45925b1e7b16944cfa98bcd9d4959bc7:function(){return Link_45925b1e7b16944cfa98bcd9d4959bc7},Link_7d0bb5237df999b20f279635c15c7e4d:function(){return Link_7d0bb5237df999b20f279635c15c7e4d},Toaster_6e90e5e87a1cac8c96c683214079bef3:function(){return Toaster_6e90e5e87a1cac8c96c683214079bef3},default:function(){return Component}});var r=n(2729),o=n(1965),c=n(7294),a=n(687),i=n(6608),l=n(9894),u=n(5711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let f=(0,u.Z)("Sun",[["circle",{cx:"12",cy:"12",r:"4",key:"4exip2"}],["path",{d:"M12 2v2",key:"tus03m"}],["path",{d:"M12 20v2",key:"1lh1kg"}],["path",{d:"m4.93 4.93 1.41 1.41",key:"149t6j"}],["path",{d:"m17.66 17.66 1.41 1.41",key:"ptbguv"}],["path",{d:"M2 12h2",key:"1t8f8n"}],["path",{d:"M20 12h2",key:"1q8mjw"}],["path",{d:"m6.34 17.66-1.41 1.41",key:"1m8zz5"}],["path",{d:"m19.07 4.93-1.41 1.41",key:"1shlcs"}]]),s=(0,u.Z)("Moon",[["path",{d:"M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z",key:"a7tn18"}]]);var d=n(917),p=n(4712),h=n(3954),b=n(3729),g=n(1664),H=n.n(g),m=n(9008),_=n.n(m);function _templateObject(){let e=(0,r._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}function Link_7d0bb5237df999b20f279635c15c7e4d(){return(0,o.tZ)(b.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},target:(0,i.oA)(!0)?"_blank":"",children:(0,o.tZ)(H(),{href:"https://reflex.dev/docs/getting-started/introduction/",passHref:!0,children:(0,o.tZ)(b.zx,{children:"Check out our docs!"})})})}function Fragment_cf53a535ae2e610a113dd361eb6ac95b(){let[e,t]=(0,c.useContext)(a.DR);return(0,o.tZ)(c.Fragment,{children:(0,i.oA)(t.length>0)?(0,o.tZ)(c.Fragment,{children:(0,o.tZ)(l.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:"".concat(v," 1s infinite")},size:32})}):(0,o.tZ)(c.Fragment,{})})}function Fragment_2e0e6a4a3aec4136eedf42fc142b7aae(){let{resolvedColorMode:e}=(0,c.useContext)(a.kc);return(0,o.tZ)(c.Fragment,{children:(0,i.oA)("light"===e)?(0,o.tZ)(c.Fragment,{children:(0,o.tZ)(f,{css:{color:"var(--current-color)"}})}):(0,o.tZ)(c.Fragment,{children:(0,o.tZ)(s,{css:{color:"var(--current-color)"}})})})}function Toaster_6e90e5e87a1cac8c96c683214079bef3(){let{resolvedColorMode:e}=(0,c.useContext)(a.kc);i.xL.__toast=p.A;let[t,n]=(0,c.useContext)(a.DR),r={description:"Check if server is reachable at ".concat((0,i.LH)(h.Ks).href),closeButton:!0,duration:12e4,id:"websocket-error"},[l,u]=(0,c.useState)(!1);return(0,c.useEffect)(()=>{n.length>=2?l||p.A.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...r,onDismiss:()=>u(!0)}):(p.A.dismiss("websocket-error"),u(!1))},[n]),(0,o.tZ)(p.x,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function Div_ac2a89ea84667d600a059f034bd91dfe(){let[e,t]=(0,c.useContext)(a.DR);return(0,o.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: ".concat(t.length>0?t[t.length-1].message:""),children:(0,o.tZ)(Fragment_cf53a535ae2e610a113dd361eb6ac95b,{})})}let v=(0,d.F4)(_templateObject());function Link_45925b1e7b16944cfa98bcd9d4959bc7(){let{resolvedColorMode:e}=(0,c.useContext)(a.kc);return(0,o.tZ)(b.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},size:"3",children:(0,o.tZ)(H(),{href:"https://reflex.dev",passHref:!0,children:(0,o.BX)(b.kC,{align:"center",className:"rx-Stack",css:{textAlign:"center",padding:"1em"},direction:"row",gap:"3",children:["Built with ",(0,o.tZ)(c.Fragment,{children:(0,i.oA)("light"===e)?(0,o.tZ)(c.Fragment,{children:(0,o.tZ)("div",{className:"rx-Html",dangerouslySetInnerHTML:{__html:'<svg width="56" height="12" viewBox="0 0 56 12" fill="none" xmlns="http://www.w3.org/2000/svg">\n<path d="M0 11.6V0.400024H8.96V4.88002H6.72V2.64002H2.24V4.88002H6.72V7.12002H2.24V11.6H0ZM6.72 11.6V7.12002H8.96V11.6H6.72Z" fill="#110F1F"/>\n<path d="M11.2 11.6V0.400024H17.92V2.64002H13.44V4.88002H17.92V7.12002H13.44V9.36002H17.92V11.6H11.2Z" fill="#110F1F"/>\n<path d="M20.16 11.6V0.400024H26.88V2.64002H22.4V4.88002H26.88V7.12002H22.4V11.6H20.16Z" fill="#110F1F"/>\n<path d="M29.12 11.6V0.400024H31.36V9.36002H35.84V11.6H29.12Z" fill="#110F1F"/>\n<path d="M38.08 11.6V0.400024H44.8V2.64002H40.32V4.88002H44.8V7.12002H40.32V9.36002H44.8V11.6H38.08Z" fill="#110F1F"/>\n<path d="M47.04 4.88002V0.400024H49.28V4.88002H47.04ZM53.76 4.88002V0.400024H56V4.88002H53.76ZM49.28 7.12002V4.88002H53.76V7.12002H49.28ZM47.04 11.6V7.12002H49.28V11.6H47.04ZM53.76 11.6V7.12002H56V11.6H53.76Z" fill="#110F1F"/>\n</svg>'}})}):(0,o.tZ)(c.Fragment,{children:(0,o.tZ)("div",{className:"rx-Html",dangerouslySetInnerHTML:{__html:'<svg width="56" height="12" viewBox="0 0 56 12" fill="none" xmlns="http://www.w3.org/2000/svg">\n<path d="M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z" fill="white"/>\n<path d="M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z" fill="white"/>\n<path d="M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z" fill="white"/>\n<path d="M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z" fill="white"/>\n<path d="M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z" fill="white"/>\n<path d="M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z" fill="white"/>\n</svg>'}})})})]})})})}function Iconbutton_126c1207e75571062288a84458b7ab68(){let{toggleColorMode:e}=(0,c.useContext)(a.kc),[t,n]=(0,c.useContext)(a.DR),r=(0,c.useCallback)(e,[t,i.ju,e]);return(0,o.tZ)(b.hU,{css:{padding:"6px",position:"fixed",top:"2rem",right:"2rem",background:"transparent",color:"inherit",zIndex:"20","&:hover":{cursor:"pointer"}},onClick:r,children:(0,o.tZ)(Fragment_2e0e6a4a3aec4136eedf42fc142b7aae,{})})}function Component(){return(0,o.BX)(c.Fragment,{children:[(0,o.BX)(c.Fragment,{children:[(0,o.tZ)(Div_ac2a89ea84667d600a059f034bd91dfe,{}),(0,o.tZ)(Toaster_6e90e5e87a1cac8c96c683214079bef3,{})]}),(0,o.BX)(b.W2,{css:{padding:"16px"},size:"3",children:[(0,o.tZ)(Iconbutton_126c1207e75571062288a84458b7ab68,{}),(0,o.BX)(b.kC,{align:"start",className:"rx-Stack",css:{minHeight:"85vh"},direction:"column",justify:"center",gap:"5",children:[(0,o.tZ)(b.X6,{size:"9",children:"Welcome to Reflex!"}),(0,o.BX)(b.xv,{as:"p",size:"5",children:["Get started by editing ",(0,o.tZ)(b.EK,{children:"Apps/Apps.py"})]}),(0,o.tZ)(Link_7d0bb5237df999b20f279635c15c7e4d,{})]}),(0,o.tZ)(b.kC,{css:{display:"flex",alignItems:"center",justifyContent:"center",width:"100%"},children:(0,o.tZ)(Link_45925b1e7b16944cfa98bcd9d4959bc7,{})})]}),(0,o.BX)(_(),{children:[(0,o.tZ)("title",{children:"Apps"}),(0,o.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}},1664:function(e,t,n){e.exports=n(5170)}},function(e){e.O(0,[534,774,888,179],function(){return e(e.s=5557)}),_N_E=e.O()}]);