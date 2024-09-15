<!doctype html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta name="twitter:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/Vorxart/AI-Agent.png" />
		<meta property="og:title" content="app.py · Vorxart/AI-Agent at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/spaces/Vorxart/AI-Agent/blob/main/app.py" />
		<meta property="og:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/Vorxart/AI-Agent.png" />

		<link rel="stylesheet" href="/front/build/kube-ea367ff/style.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>

		<link
			rel="preload"
			href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css"
			as="style"
			onload="this.onload=null;this.rel='stylesheet'"
		/>
		<noscript>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css" />
		</noscript>

		<link rel="canonical" href="https://huggingface.co/spaces/Vorxart/AI-Agent/blob/main/app.py">  <!-- HEAD_svelte-1oal594_START --><style>.blob-line-num::before {
			content: attr(data-line-num);
		}
	</style><!-- HEAD_svelte-1oal594_END -->

		<title>app.py · Vorxart/AI-Agent at main</title>

		<script
			defer
			data-domain="huggingface.co"
			event-loggedIn="true"
			src="/js/script.pageview-props.js"
		></script>
		<script>
			window.plausible =
				window.plausible ||
				function () {
					(window.plausible.q = window.plausible.q || []).push(arguments);
				};
		</script>
		<script>
			window.hubConfig = JSON.parse(`{"features":{"signupDisabled":false},"sshGitUrl":"git@hf.co","moonHttpUrl":"https://huggingface.co","captchaApiKey":"bd5f2066-93dc-4bdd-a64b-a24646ca3859","captchaDisabledOnSignup":true,"datasetViewerPublicUrl":"https://datasets-server.huggingface.co","stripePublicKey":"pk_live_x2tdjFXBCvXo2FFmMybezpeM00J6gPCAAc","environment":"production","userAgent":"HuggingFace (production)","spacesIframeDomain":"hf.space","spacesApiUrl":"https://api.hf.space","docSearchKey":"ece5e02e57300e17d152c08056145326e90c4bff3dd07d7d1ae40cf1c8d39cb6","logoDev":{"apiUrl":"https://img.logo.dev/","apiKey":"pk_UHS2HZOeRnaSOdDp7jbd5w"}}`);
		</script>
		<script type="text/javascript" src="https://de5282c3ca0c.edge.sdk.awswaf.com/de5282c3ca0c/526cf06acb0d/challenge.js" defer></script>
	</head>
	<body class="flex flex-col min-h-dvh bg-white dark:bg-gray-950 text-black ViewerBlobPage">
		<div class="flex min-h-dvh flex-col">
	<div class="SVELTE_HYDRATER contents" data-target="MainHeader" data-props="{&quot;authLight&quot;:{&quot;csrfToken&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MjYzOTU4MTg0OTMsInVzZXJJZCI6IjY2Yzk4YmNkMzE1YWYwNjhhOWYwMGJiMSJ9LCJzaWduYXR1cmUiOiJlNjQ5YmE2ZjUwNjYyMTBlOWUzOWVhMTcwZjIxODRmNWM1YjY3OGY3ZjQ3NjlhMzFjYzc2Y2NjNzkxMjI2YWIxIn0=&quot;,&quot;hasHfLevelAccess&quot;:false,&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/ea972415da005855798d70b72ae5f8f2.svg&quot;,&quot;isPro&quot;:false,&quot;orgs&quot;:[],&quot;user&quot;:&quot;Vorxart&quot;,&quot;canPost&quot;:false,&quot;canHaveBilling&quot;:true,&quot;canCreateOrg&quot;:true,&quot;theme&quot;:&quot;light&quot;,&quot;notifications&quot;:{&quot;org_suggestions&quot;:false}}},&quot;classNames&quot;:&quot;&quot;,&quot;avatarUrl&quot;:&quot;/avatars/ea972415da005855798d70b72ae5f8f2.svg&quot;,&quot;isWide&quot;:false,&quot;isZh&quot;:false,&quot;user&quot;:&quot;Vorxart&quot;,&quot;unreadNotifications&quot;:0,&quot;csrf&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MjYzOTU4MTg0OTMsInVzZXJJZCI6IjY2Yzk4YmNkMzE1YWYwNjhhOWYwMGJiMSJ9LCJzaWduYXR1cmUiOiJlNjQ5YmE2ZjUwNjYyMTBlOWUzOWVhMTcwZjIxODRmNWM1YjY3OGY3ZjQ3NjlhMzFjYzc2Y2NjNzkxMjI2YWIxIn0=&quot;,&quot;canCreateOrg&quot;:true}"><header class="border-b border-gray-100 "><div class="w-full px-4 container flex h-16 items-center"><div class="flex flex-1 items-center"><a class="mr-5 flex flex-none items-center lg:mr-6" href="/"><img alt="Hugging Face's logo" class="w-7 md:mr-2" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden whitespace-nowrap text-lg font-bold md:block">Hugging Face</span></a>
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 md:mr-3 xl:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 pl-8 form-input-alt h-9 pr-3 focus:shadow-xl " name="" placeholder="Search models, datasets, users..."   spellcheck="false" type="text" value="">
	<svg class="absolute left-2.5 text-gray-400 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<div class="flex flex-none items-center justify-center p-0.5 place-self-stretch lg:hidden"><button class="relative z-40 flex h-6 w-8 items-center justify-center" type="button"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-xl" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg>
		</button>

	</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-1.5 xl:space-x-2"><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-indigo-700" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
					Models</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-red-700" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					Datasets</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-blue-700" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
					Spaces</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/posts"><svg class="mr-1.5 text-gray-400 group-hover:text-yellow-500 !text-yellow-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 12 12" preserveAspectRatio="xMidYMid meet"><path fill="currentColor" fill-rule="evenodd" d="M3.73 2.4A4.25 4.25 0 1 1 6 10.26H2.17l-.13-.02a.43.43 0 0 1-.3-.43l.01-.06a.43.43 0 0 1 .12-.22l.84-.84A4.26 4.26 0 0 1 3.73 2.4Z" clip-rule="evenodd"></path></svg>
					Posts</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path opacity="0.5" d="M20.9022 5.10334L10.8012 10.8791L7.76318 9.11193C8.07741 8.56791 8.5256 8.11332 9.06512 7.7914L15.9336 3.73907C17.0868 3.08811 18.5002 3.26422 19.6534 3.91519L19.3859 3.73911C19.9253 4.06087 20.5879 4.56025 20.9022 5.10334Z" fill="currentColor"></path><path d="M10.7999 10.8792V28.5483C10.2136 28.5475 9.63494 28.4139 9.10745 28.1578C8.5429 27.8312 8.074 27.3621 7.74761 26.7975C7.42122 26.2327 7.24878 25.5923 7.24756 24.9402V10.9908C7.25062 10.3319 7.42358 9.68487 7.74973 9.1123L10.7999 10.8792Z" fill="currentColor" fill-opacity="0.75"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M21.3368 10.8499V6.918C21.3331 6.25959 21.16 5.61234 20.8346 5.03949L10.7971 10.8727L10.8046 10.874L21.3368 10.8499Z" fill="currentColor"></path><path opacity="0.5" d="M21.7937 10.8488L10.7825 10.8741V28.5486L21.7937 28.5234C23.3344 28.5234 24.5835 27.2743 24.5835 25.7335V13.6387C24.5835 12.0979 23.4365 11.1233 21.7937 10.8488Z" fill="currentColor"></path></svg>
					Docs</a>
			</li>
		<li class="max-2xl:hidden"><div class="relative ">
	<button class="px-2 py-0.5 group hover:text-green-700 dark:hover:text-gray-400 flex items-center " type="button">
		<svg class="mr-1.5 text-gray-400 group-hover:text-green-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1h2zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14H8.837z" fill="currentColor"></path></svg>
			Solutions
		</button>
	
	
	</div></li>
		<li><a class="group flex items-center px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/pricing">Pricing
			</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center " type="button">
		<svg class=" text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	</div></li>
		<li><hr class="h-5 w-0.5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><form action="/logout" method="POST" class="hidden"><input type="hidden" name="csrf" value="eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MjYzOTU4MTg0OTMsInVzZXJJZCI6IjY2Yzk4YmNkMzE1YWYwNjhhOWYwMGJiMSJ9LCJzaWduYXR1cmUiOiJlNjQ5YmE2ZjUwNjYyMTBlOWUzOWVhMTcwZjIxODRmNWM1YjY3OGY3ZjQ3NjlhMzFjYzc2Y2NjNzkxMjI2YWIxIn0="></form>
<div class="relative ml-2 w-[1.38rem] h-[1.38rem] ">
	<button class="ml-auto rounded-full ring-2 group ring-indigo-400 focus:ring-blue-500 hover:ring-offset-1 focus:ring-offset-1 focus:outline-none outline-none dark:ring-offset-gray-950 " type="button">
		
		<div class="relative"><img alt="" class="h-[1.38rem] w-[1.38rem] overflow-hidden rounded-full" src="/avatars/ea972415da005855798d70b72ae5f8f2.svg" crossorigin="anonymous">
			</div>
	
		</button>
	
	
	</div></li></ul></nav></div></header></div>
	
	
	
	<div class="SVELTE_HYDRATER contents" data-target="SSOBanner" data-props="{&quot;organizations&quot;:[]}"></div>
	

	<main class="flex flex-1 flex-col"><div class="SVELTE_HYDRATER contents" data-target="SpaceHeader" data-props="{&quot;activeTab&quot;:&quot;files&quot;,&quot;authLight&quot;:{&quot;csrfToken&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MjYzOTU4MTg0OTMsInVzZXJJZCI6IjY2Yzk4YmNkMzE1YWYwNjhhOWYwMGJiMSJ9LCJzaWduYXR1cmUiOiJlNjQ5YmE2ZjUwNjYyMTBlOWUzOWVhMTcwZjIxODRmNWM1YjY3OGY3ZjQ3NjlhMzFjYzc2Y2NjNzkxMjI2YWIxIn0=&quot;,&quot;hasHfLevelAccess&quot;:false,&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/ea972415da005855798d70b72ae5f8f2.svg&quot;,&quot;isPro&quot;:false,&quot;orgs&quot;:[],&quot;user&quot;:&quot;Vorxart&quot;,&quot;canPost&quot;:false,&quot;canHaveBilling&quot;:true,&quot;canCreateOrg&quot;:true,&quot;theme&quot;:&quot;light&quot;,&quot;notifications&quot;:{&quot;org_suggestions&quot;:false}}},&quot;author&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/ea972415da005855798d70b72ae5f8f2.svg&quot;,&quot;fullname&quot;:&quot;Ibrahim &quot;,&quot;name&quot;:&quot;Vorxart&quot;,&quot;type&quot;:&quot;user&quot;,&quot;isPro&quot;:false,&quot;isHf&quot;:false,&quot;isMod&quot;:false},&quot;canDisable&quot;:false,&quot;canReadRepoSettings&quot;:true,&quot;canWriteRepoSettings&quot;:true,&quot;discussionsStats&quot;:{&quot;closed&quot;:0,&quot;open&quot;:0,&quot;total&quot;:0},&quot;query&quot;:{},&quot;space&quot;:{&quot;author&quot;:&quot;Vorxart&quot;,&quot;colorFrom&quot;:&quot;purple&quot;,&quot;colorTo&quot;:&quot;pink&quot;,&quot;cardData&quot;:{&quot;title&quot;:&quot;AI Agent&quot;,&quot;emoji&quot;:&quot;👁&quot;,&quot;colorFrom&quot;:&quot;purple&quot;,&quot;colorTo&quot;:&quot;pink&quot;,&quot;sdk&quot;:&quot;streamlit&quot;,&quot;sdk_version&quot;:&quot;1.38.0&quot;,&quot;app_file&quot;:&quot;app.py&quot;,&quot;pinned&quot;:false,&quot;license&quot;:&quot;mit&quot;},&quot;createdAt&quot;:&quot;2024-09-10T05:38:17.000Z&quot;,&quot;emoji&quot;:&quot;👁&quot;,&quot;discussionsDisabled&quot;:false,&quot;duplicationDisabled&quot;:false,&quot;id&quot;:&quot;Vorxart/AI-Agent&quot;,&quot;isLikedByUser&quot;:false,&quot;isMutedByUser&quot;:false,&quot;isWatchedByUser&quot;:true,&quot;lastModified&quot;:&quot;2024-09-14T10:11:31.000Z&quot;,&quot;likes&quot;:0,&quot;pinned&quot;:false,&quot;private&quot;:false,&quot;gated&quot;:false,&quot;repoType&quot;:&quot;space&quot;,&quot;subdomain&quot;:&quot;vorxart-ai-agent&quot;,&quot;sdk&quot;:&quot;streamlit&quot;,&quot;sdkVersion&quot;:&quot;1.38.0&quot;,&quot;title&quot;:&quot;AI Agent&quot;,&quot;runtime&quot;:{&quot;stage&quot;:&quot;RUNNING&quot;,&quot;hardware&quot;:{&quot;current&quot;:&quot;cpu-basic&quot;,&quot;requested&quot;:&quot;cpu-basic&quot;},&quot;storage&quot;:null,&quot;gcTimeout&quot;:172800,&quot;replicas&quot;:{&quot;current&quot;:1,&quot;requested&quot;:1},&quot;devMode&quot;:false,&quot;domains&quot;:[{&quot;domain&quot;:&quot;vorxart-ai-agent.hf.space&quot;,&quot;isCustom&quot;:false,&quot;stage&quot;:&quot;READY&quot;}],&quot;sha&quot;:&quot;6a6b7cf67d822341e7a1cac651fe588d7d38321c&quot;},&quot;iframe&quot;:{&quot;embedSrc&quot;:&quot;https://vorxart-ai-agent.hf.space&quot;,&quot;src&quot;:&quot;https://vorxart-ai-agent.hf.space&quot;},&quot;secrets&quot;:[{&quot;key&quot;:&quot;AIML_API_KEY&quot;,&quot;updatedAt&quot;:&quot;2024-09-12T02:49:05.338Z&quot;}],&quot;variables&quot;:[],&quot;sse&quot;:{&quot;url&quot;:&quot;https://api.hf.space/v1/Vorxart/AI-Agent&quot;,&quot;jwt&quot;:&quot;eyJhbGciOiJFZERTQSJ9.eyJyZWFkIjp0cnVlLCJwZXJtaXNzaW9ucyI6eyJyZXBvLmNvbnRlbnQucmVhZCI6dHJ1ZX0sIm9uQmVoYWxmT2YiOnsia2luZCI6InVzZXIiLCJfaWQiOiI2NmM5OGJjZDMxNWFmMDY4YTlmMDBiYjEiLCJ1c2VyIjoiVm9yeGFydCJ9LCJpYXQiOjE3MjYzMDk0MTgsInN1YiI6Ii9zcGFjZXMvVm9yeGFydC9BSS1BZ2VudCIsImV4cCI6MTcyNjM5NTgxOCwiaXNzIjoiaHR0cHM6Ly9odWdnaW5nZmFjZS5jbyJ9.XwNet3hZMxHKzMDYQbGqEf3qqU-78faPS87hXn11G_Np0oM1hxIunmIIgiFKS7jV7ekEZMNmB_pSTUBsg2AcBA&quot;},&quot;dockerJwt&quot;:&quot;eyJhbGciOiJFZERTQSJ9.eyJyZWFkIjp0cnVlLCJwZXJtaXNzaW9ucyI6eyJyZXBvLmNvbnRlbnQucmVhZCI6dHJ1ZX0sIm9uQmVoYWxmT2YiOnsia2luZCI6InVzZXIiLCJfaWQiOiI2NmM5OGJjZDMxNWFmMDY4YTlmMDBiYjEiLCJ1c2VyIjoiVm9yeGFydCJ9LCJpYXQiOjE3MjYzMDk0MTgsInN1YiI6Ii9zcGFjZXMvVm9yeGFydC9BSS1BZ2VudCIsImV4cCI6MTcyNjM5NTgxOCwiaXNzIjoiaHR0cHM6Ly9odWdnaW5nZmFjZS5jbyJ9.XwNet3hZMxHKzMDYQbGqEf3qqU-78faPS87hXn11G_Np0oM1hxIunmIIgiFKS7jV7ekEZMNmB_pSTUBsg2AcBA&quot;,&quot;linkedModels&quot;:[],&quot;linkedDatasets&quot;:[],&quot;linkedCollections&quot;:[],&quot;sha&quot;:&quot;6a6b7cf67d822341e7a1cac651fe588d7d38321c&quot;,&quot;hasBlockedOids&quot;:false},&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/ea972415da005855798d70b72ae5f8f2.svg&quot;,&quot;isPro&quot;:false,&quot;fullname&quot;:&quot;Ibrahim &quot;,&quot;user&quot;:&quot;Vorxart&quot;,&quot;orgs&quot;:[],&quot;signup&quot;:{&quot;github&quot;:&quot;IIPatel&quot;},&quot;isHf&quot;:false,&quot;isMod&quot;:false,&quot;type&quot;:&quot;user&quot;,&quot;canPay&quot;:false,&quot;spacesAvailableFlavors&quot;:[&quot;cpu-basic&quot;,&quot;zero-a10g&quot;,&quot;cpu-upgrade&quot;,&quot;t4-small&quot;,&quot;t4-medium&quot;,&quot;l4x1&quot;,&quot;l4x4&quot;,&quot;l40sx1&quot;,&quot;l40sx4&quot;,&quot;l40sx8&quot;,&quot;a10g-small&quot;,&quot;a10g-large&quot;,&quot;a10g-largex2&quot;,&quot;a10g-largex4&quot;,&quot;a100-large&quot;,&quot;v5e-1x1&quot;,&quot;v5e-2x2&quot;,&quot;v5e-2x4&quot;],&quot;canPost&quot;:false}}">

<header class="from-gray-50-to-white border-b border-gray-100 bg-gradient-to-t via-white dark:via-gray-950 pt-4 xl:pt-0"><div class="container relative flex flex-col xl:flex-row"><h1 class="flex flex-wrap items-center leading-tight gap-y-1 text-lg xl:flex-none"><a href="/spaces" class="group flex items-center"><svg class="mr-1 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M7.80914 18.7462V24.1907H13.2536V18.7462H7.80914Z" fill="#FF3270"></path><path d="M18.7458 18.7462V24.1907H24.1903V18.7462H18.7458Z" fill="#861FFF"></path><path d="M7.80914 7.80982V13.2543H13.2536V7.80982H7.80914Z" fill="#097EFF"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M4 6.41775C4 5.08246 5.08246 4 6.41775 4H14.6457C15.7626 4 16.7026 4.75724 16.9802 5.78629C18.1505 4.67902 19.7302 4 21.4685 4C25.0758 4 28.0003 6.92436 28.0003 10.5317C28.0003 12.27 27.3212 13.8497 26.2139 15.02C27.243 15.2977 28.0003 16.2376 28.0003 17.3545V25.5824C28.0003 26.9177 26.9177 28.0003 25.5824 28.0003H17.0635H14.9367H6.41775C5.08246 28.0003 4 26.9177 4 25.5824V15.1587V14.9367V6.41775ZM7.80952 7.80952V13.254H13.254V7.80952H7.80952ZM7.80952 24.1907V18.7462H13.254V24.1907H7.80952ZM18.7462 24.1907V18.7462H24.1907V24.1907H18.7462ZM18.7462 10.5317C18.7462 9.0283 19.9651 7.80952 21.4685 7.80952C22.9719 7.80952 24.1907 9.0283 24.1907 10.5317C24.1907 12.0352 22.9719 13.254 21.4685 13.254C19.9651 13.254 18.7462 12.0352 18.7462 10.5317Z" fill="black"></path><path d="M21.4681 7.80982C19.9647 7.80982 18.7458 9.02861 18.7458 10.5321C18.7458 12.0355 19.9647 13.2543 21.4681 13.2543C22.9715 13.2543 24.1903 12.0355 24.1903 10.5321C24.1903 9.02861 22.9715 7.80982 21.4681 7.80982Z" fill="#FFD702"></path></svg>
					<span class="mr-2.5 font-semibold text-gray-400 group-hover:text-gray-500">Spaces:</span></a>
			<div class="group flex flex-none items-center"><div class="relative mr-1.5 flex items-center">

			<img alt="" class="w-3.5 h-3.5 rounded-full  flex-none" src="/avatars/ea972415da005855798d70b72ae5f8f2.svg" crossorigin="anonymous"></div>
		<a href="/Vorxart" class="text-gray-400 hover:text-blue-600">Vorxart</a>
		<div class="mx-0.5 text-gray-300">/</div></div>

<div class="max-w-full xl:flex xl:min-w-0 xl:flex-nowrap xl:items-center xl:gap-x-1"><a class="break-words font-mono font-semibold hover:text-blue-600 text-[1.07rem] xl:truncate" href="/spaces/Vorxart/AI-Agent">AI-Agent</a>
	<button class="relative text-xs mr-3  inline-flex cursor-pointer items-center text-sm focus:outline-none  mx-0.5   text-gray-600 " title="Copy space name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div>
			<div class="inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white text-sm leading-none text-gray-500  mr-2"><button class="relative flex items-center overflow-hidden from-red-50 to-transparent dark:from-red-900 px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none"  title="Like"><svg class="left-1.5 absolute" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		
		<span class="ml-4 pl-0.5 ">like</span></button>
	<button class="flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 focus:outline-none dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="See users who liked this repository">0</button></div>


			



<span class="inline-block "><span class="contents"><div class="inline-flex cursor-pointer select-none items-center overflow-hidden font-mono text-xs flex-shrink-0 mr-2 rounded-lg border leading-none dark:bg-gray-900
					border-green-100 
					text-green-700 dark:text-green-500"><div class="inline-flex items-center px-2 py-[0.32rem] dark:bg-gray-900  border-green-100 bg-green-50 hover:bg-green-100/70 hover:text-green-800 dark:hover:text-green-400">
					<div class="ml-0.5 mr-1.5 inline-block h-1.5 w-1.5 animate-pulse rounded-full bg-green-500"></div>
		Running
		</div>
	</div></span>

	</span>

	<button class="mr-2 inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white px-1.5 py-1 text-sm leading-none text-gray-500 hover:bg-gray-50 focus:bg-gray-100 focus:outline-none dark:hover:bg-gray-900 dark:focus:bg-gray-800"><svg class="2xl:mr-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M4 6h18v2H4zm0 6h18v2H4zm0 6h12v2H4zm17 0l7 5l-7 5V18z"></path></svg><span class="hidden 2xl:block">Logs</span></button>


			
			

<div class="sm:hidden"><div class="relative ">
	<button class="btn px-1 py-1 text-sm translate-y-0 " type="button">
		
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="p-px" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><circle cx="16" cy="7" r="3" fill="currentColor"></circle><circle cx="16" cy="16" r="3" fill="currentColor"></circle><circle cx="16" cy="25" r="3" fill="currentColor"></circle></svg>
			
		
		</button>
	
	
	</div></div>



</h1>
		

		<div class="flex flex-col-reverse gap-x-2 sm:flex-row sm:items-center sm:justify-between xl:ml-auto"><div class="-mb-px flex h-12 items-center overflow-x-auto overflow-y-hidden sm:h-[3.25rem]"><a class="tab-alternate " href="/spaces/Vorxart/AI-Agent"><svg class="mr-1.5 text-gray-400 flex-none" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
			App
			
			
		</a><a class="tab-alternate active" href="/spaces/Vorxart/AI-Agent/tree/main"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
			<span class="xl:hidden">Files</span>
				<span class="hidden xl:inline">Files</span>
			
			
		</a><a class="tab-alternate " href="/spaces/Vorxart/AI-Agent/discussions"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
			Community
			
			
		</a><a class="tab-alternate " href="/spaces/Vorxart/AI-Agent/settings"><svg class="opacity-50 dark:opacity-70 mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25" fill="currentColor"><path d="M13.0101 3C13.7157 3.0078 14.4184 3.09062 15.1077 3.24652C15.2543 3.2797 15.3871 3.35848 15.4874 3.47186C15.5877 3.58523 15.6506 3.72754 15.6672 3.8789L15.8306 5.36678C15.8537 5.57655 15.925 5.77791 16.0389 5.95464C16.1527 6.13137 16.3059 6.27854 16.4861 6.38432C16.6663 6.4901 16.8685 6.55153 17.0764 6.56367C17.2843 6.57581 17.4921 6.53831 17.6831 6.4542L19.0299 5.85495C19.1667 5.79391 19.3187 5.77743 19.4651 5.8078C19.6115 5.83818 19.745 5.9139 19.847 6.02449C20.8199 7.07789 21.5443 8.3412 21.9658 9.71937C22.01 9.8642 22.0087 10.0194 21.962 10.1634C21.9153 10.3074 21.8256 10.4332 21.7053 10.5232L20.5113 11.4158C20.3434 11.5408 20.2069 11.7041 20.1128 11.8925C20.0187 12.0809 19.9697 12.2891 19.9697 12.5003C19.9697 12.7114 20.0187 12.9196 20.1128 13.108C20.2069 13.2964 20.3434 13.4597 20.5113 13.5848L21.7062 14.4763C21.8269 14.5663 21.917 14.6922 21.9638 14.8364C22.0107 14.9806 22.0121 15.1361 21.9677 15.2812C21.546 16.6593 20.8216 17.9225 19.849 18.976C19.7471 19.0864 19.6141 19.162 19.4681 19.1926C19.3221 19.2231 19.1704 19.207 19.0338 19.1466L17.6812 18.5454C17.4904 18.4606 17.2827 18.4225 17.0748 18.4343C16.8668 18.446 16.6645 18.5072 16.4842 18.6129C16.3039 18.7185 16.1508 18.8658 16.037 19.0426C15.9233 19.2195 15.8523 19.421 15.8297 19.6308L15.6672 21.1177C15.6508 21.2674 15.5892 21.4084 15.4908 21.5212C15.3923 21.6341 15.2619 21.7133 15.1173 21.7482C13.7249 22.0839 12.2742 22.0839 10.8817 21.7482C10.7371 21.7133 10.6067 21.6341 10.5083 21.5212C10.4098 21.4084 10.3482 21.2674 10.3318 21.1177L10.1703 19.6328C10.1468 19.4235 10.0751 19.2227 9.96107 19.0465C9.84703 18.8704 9.69381 18.7238 9.51373 18.6186C9.33364 18.5134 9.13172 18.4525 8.92419 18.4408C8.71666 18.4291 8.50931 18.4669 8.31882 18.5512L6.9672 19.1514C6.83048 19.2121 6.67854 19.2283 6.53235 19.1978C6.38616 19.1672 6.25292 19.0915 6.15103 18.9809C5.17789 17.9263 4.45346 16.6616 4.03227 15.2821C3.98795 15.1371 3.98931 14.9816 4.03617 14.8374C4.08304 14.6931 4.17306 14.5673 4.29375 14.4773L5.48868 13.5848C5.65676 13.4599 5.79345 13.2966 5.88768 13.1082C5.9819 12.9198 6.031 12.7115 6.031 12.5003C6.031 12.289 5.9819 12.0808 5.88768 11.8923C5.79345 11.7039 5.65676 11.5407 5.48868 11.4158L4.29375 10.5252C4.17324 10.4351 4.0834 10.3092 4.03671 10.1649C3.99003 10.0207 3.98881 9.8653 4.03323 9.72034C4.45479 8.34219 5.17922 7.07889 6.15199 6.02547C6.25407 5.91487 6.38753 5.83915 6.53391 5.80878C6.6803 5.77841 6.83238 5.79488 6.96912 5.85593L8.31498 6.45517C8.5063 6.53923 8.71441 6.57664 8.92258 6.56439C9.13075 6.55214 9.33319 6.49057 9.51363 6.38462C9.69406 6.27868 9.84747 6.13132 9.96152 5.95438C10.0756 5.77744 10.1471 5.57585 10.1703 5.36581L10.3338 3.8789C10.3503 3.72724 10.4132 3.58462 10.5137 3.47103C10.6142 3.35745 10.7473 3.2786 10.8942 3.24555C11.5835 3.09062 12.2881 3.00877 13.0101 3ZM12.9986 9.57711C12.2337 9.57711 11.5001 9.88508 10.9593 10.4333C10.4184 10.9815 10.1146 11.725 10.1146 12.5003C10.1146 13.2755 10.4184 14.0191 10.9593 14.5672C11.5001 15.1154 12.2337 15.4234 12.9986 15.4234C13.7634 15.4234 14.497 15.1154 15.0378 14.5672C15.5787 14.0191 15.8825 13.2755 15.8825 12.5003C15.8825 11.725 15.5787 10.9815 15.0378 10.4333C14.497 9.88508 13.7634 9.57711 12.9986 9.57711Z"></path></svg>
			Settings
			
			
		</a>
	</div>
		
			

<div class="hidden sm:block mt-2 lg:mt-0"><div class="relative ">
	<button class="btn px-1 py-1 text-base translate-y-px " type="button">
		
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="p-0.5" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><circle cx="16" cy="7" r="3" fill="currentColor"></circle><circle cx="16" cy="16" r="3" fill="currentColor"></circle><circle cx="16" cy="25" r="3" fill="currentColor"></circle></svg>
			
		
		</button>
	
	
	</div></div>




		</div></div></header>

























	



</div>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full md:grid-cols-12  space-y-4 md:gap-6 mb-16"><section class="pt-8 border-gray-100 col-span-full"><header class="flex flex-wrap items-center justify-start pb-2 md:justify-end lg:flex-nowrap"><div class="relative mr-4 flex min-w-0 basis-auto flex-wrap items-center md:flex-grow md:basis-full lg:basis-auto lg:flex-nowrap"><div class="SVELTE_HYDRATER contents" data-target="BranchSelector" data-props="{&quot;path&quot;:&quot;app.py&quot;,&quot;repoName&quot;:&quot;Vorxart/AI-Agent&quot;,&quot;repoType&quot;:&quot;space&quot;,&quot;rev&quot;:&quot;main&quot;,&quot;refs&quot;:{&quot;branches&quot;:[{&quot;name&quot;:&quot;main&quot;,&quot;ref&quot;:&quot;refs/heads/main&quot;,&quot;targetCommit&quot;:&quot;6a6b7cf67d822341e7a1cac651fe588d7d38321c&quot;}],&quot;tags&quot;:[],&quot;converts&quot;:[]},&quot;view&quot;:&quot;blob&quot;}"><div class="relative mr-4 mb-2">
	<button class="text-sm md:text-base btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div></div>
		<div class="relative mb-2 flex flex-wrap items-center"><a class="truncate text-gray-800 hover:underline" href="/spaces/Vorxart/AI-Agent/tree/main">AI-Agent</a>
			<span class="mx-1 text-gray-300">/</span>
				<span class="dark:text-gray-300">app.py</span>
				<div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;app.py&quot;,&quot;classNames&quot;:&quot;text-xs ml-2&quot;,&quot;title&quot;:&quot;Copy path&quot;}"><button class="relative text-xs ml-2 inline-flex cursor-pointer items-center text-sm focus:outline-none  mx-0.5   text-gray-600 " title="Copy path" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div></div></div>

	
	</header>
			<div class="SVELTE_HYDRATER contents" data-target="LastCommit" data-props="{&quot;commitLast&quot;:{&quot;date&quot;:&quot;2024-09-14T10:11:31.000Z&quot;,&quot;verified&quot;:&quot;verified&quot;,&quot;subject&quot;:&quot;Update app.py&quot;,&quot;authors&quot;:[{&quot;_id&quot;:&quot;66c98bcd315af068a9f00bb1&quot;,&quot;avatar&quot;:&quot;/avatars/ea972415da005855798d70b72ae5f8f2.svg&quot;,&quot;isHf&quot;:false,&quot;user&quot;:&quot;Vorxart&quot;}],&quot;commit&quot;:{&quot;id&quot;:&quot;6a6b7cf67d822341e7a1cac651fe588d7d38321c&quot;,&quot;parentIds&quot;:[&quot;0fc5c33b3e3f8c9fd022d5fe391e63b45c40ddb6&quot;]},&quot;title&quot;:&quot;Update app.py&quot;},&quot;repo&quot;:{&quot;name&quot;:&quot;Vorxart/AI-Agent&quot;,&quot;type&quot;:&quot;space&quot;}}"><div class="from-gray-100-to-white flex items-baseline rounded-t-lg border border-b-0 bg-gradient-to-t px-3 py-2 dark:border-gray-800"><img class="mr-2.5 mt-0.5 h-4 w-4 self-center rounded-full" alt="Vorxart's picture" src="/avatars/ea972415da005855798d70b72ae5f8f2.svg">
			<div class="mr-5 flex flex-none items-center truncate"><a class="hover:underline" href="/Vorxart">Vorxart
					</a>
				
			</div>
		<div class="mr-4 truncate font-mono text-sm text-gray-500 hover:prose-a:underline"><!-- HTML_TAG_START -->Update app.py<!-- HTML_TAG_END --></div>
		<a class="rounded border bg-gray-50 px-1.5 text-sm hover:underline dark:border-gray-800 dark:bg-gray-900" href="/spaces/Vorxart/AI-Agent/commit/6a6b7cf67d822341e7a1cac651fe588d7d38321c">6a6b7cf</a>
		<span class="mx-2 text-green-500 dark:text-green-600 px-1.5 border-green-100 dark:border-green-800 rounded-full border text-xs uppercase" title="This commit is signed and the signature is verified">verified</span>
		<time class="ml-auto hidden flex-none truncate pl-2 text-gray-500 dark:text-gray-400 lg:block" datetime="2024-09-14T10:11:31" title="Sat, 14 Sep 2024 10:11:31 GMT">12 minutes ago</time></div></div>
			<div class="flex flex-wrap items-center border px-3 py-1.5 text-sm text-gray-800 dark:border-gray-800 dark:bg-gray-900">
				<a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/Vorxart/AI-Agent/raw/main/app.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
							raw
						</a><div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;https://huggingface.co/spaces/Vorxart/AI-Agent/resolve/main/app.py&quot;,&quot;style&quot;:&quot;blank&quot;,&quot;label&quot;:&quot;Copy download link&quot;,&quot;classNames&quot;:&quot;my-1 mr-4 flex items-center no-underline hover:underline&quot;}"><button class="relative my-1 mr-4 flex items-center no-underline hover:underline       " title="Copy download link" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	<span class="ml-1.5 ">Copy download link</span>
	</button></div><a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/Vorxart/AI-Agent/commits/main/app.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
							history
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/Vorxart/AI-Agent/blame/main/app.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
							blame
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/Vorxart/AI-Agent/edit/main/app.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M2 26h28v2H2z" fill="currentColor"></path><path d="M25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4l15-15zm-5-5L24 7.6l-3 3L17.4 7l3-3zM6 22v-3.6l10-10l3.6 3.6l-10 10H6z" fill="currentColor"></path></svg>
							edit
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/Vorxart/AI-Agent/delete/main/app.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12 12h2v12h-2z" fill="currentColor"></path><path d="M18 12h2v12h-2z" fill="currentColor"></path><path d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20z" fill="currentColor"></path><path d="M12 2h8v2h-8z" fill="currentColor"></path></svg>
							delete
						</a>
				
				
				<div class="flex items-center gap-x-3 dark:text-gray-300 sm:ml-auto"><div class="SVELTE_HYDRATER contents" data-target="LineWrapButton" data-props="{&quot;classNames&quot;:&quot;text-xs&quot;,&quot;lineSelectorClass&quot;:&quot;blob-line&quot;}">

<button class="text-xs" type="button" title="Toggle Line Wrap"><svg class="opacity-50" width="1em" height="1em" viewBox="0 0 12 11" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.75 1.25H11.25M0.75 5H9C9.75 5 11.25 5.375 11.25 6.875C11.25 8.375 9.99975 8.75 9.375 8.75H6M6 8.75L7.5 7.25M6 8.75L7.5 10.25M0.75 8.75H3.75" stroke="currentColor" stroke-width="1.125" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div>
					13.4 kB</div></div>

			<div class="relative min-h-[100px] rounded-b-lg border border-t-0 leading-tight dark:border-gray-800 dark:bg-gray-925">
				<div class="py-3"><div class="SVELTE_HYDRATER contents" data-target="BlobContent" data-props="{&quot;lines&quot;:[&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> streamlit <span class=\&quot;hljs-keyword\&quot;>as</span> st&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> openai&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> os&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> pandas <span class=\&quot;hljs-keyword\&quot;>as</span> pd&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> numpy <span class=\&quot;hljs-keyword\&quot;>as</span> np&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> matplotlib.pyplot <span class=\&quot;hljs-keyword\&quot;>as</span> plt&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> streamlit_option_menu <span class=\&quot;hljs-keyword\&quot;>import</span> option_menu&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> streamlit_folium <span class=\&quot;hljs-keyword\&quot;>import</span> folium_static&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> folium&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> plotly.express <span class=\&quot;hljs-keyword\&quot;>as</span> px&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> wordcloud <span class=\&quot;hljs-keyword\&quot;>import</span> WordCloud&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Set up OpenAI client</span>&quot;,&quot;openai.api_key = os.getenv(<span class=\&quot;hljs-string\&quot;>&amp;quot;AIML_API_KEY&amp;quot;</span>)&quot;,&quot;openai.api_base = <span class=\&quot;hljs-string\&quot;>&amp;quot;https://api.aimlapi.com&amp;quot;</span>&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Initialize session state variables</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span> <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-keyword\&quot;>in</span> st.session_state:&quot;,&quot;    st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span>] = [&quot;,&quot;        {<span class=\&quot;hljs-string\&quot;>&amp;quot;role&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;system&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;content&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;You are an AI assistant specializing in the circular economy. You provide insightful, practical, and innovative solutions to enhance sustainability and resource efficiency. You communicate in a clear and engaging manner, making complex topics easy to understand.&amp;quot;</span>}&quot;,&quot;    ]&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-string\&quot;>&amp;#x27;resources&amp;#x27;</span> <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-keyword\&quot;>in</span> st.session_state:&quot;,&quot;    st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;resources&amp;#x27;</span>] = []&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Define functions (keep existing functions and add new ones)</span>&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Define a function to generate a response from the AI</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>generate_response</span>(<span class=\&quot;hljs-params\&quot;>prompt, model=<span class=\&quot;hljs-string\&quot;>&amp;quot;meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo&amp;quot;</span></span>):&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Add user message to the conversation history</span>&quot;,&quot;        st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span>].append({<span class=\&quot;hljs-string\&quot;>&amp;quot;role&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;user&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;content&amp;quot;</span>: prompt})&quot;,&quot;        &quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Generate response from the AI</span>&quot;,&quot;        response = openai.ChatCompletion.create(&quot;,&quot;            model=model,&quot;,&quot;            messages=st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span>]&quot;,&quot;        )&quot;,&quot;        &quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Extract the AI response</span>&quot;,&quot;        ai_response = response.choices[<span class=\&quot;hljs-number\&quot;>0</span>].message[<span class=\&quot;hljs-string\&quot;>&amp;#x27;content&amp;#x27;</span>]&quot;,&quot;        &quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Add AI response to the conversation history</span>&quot;,&quot;        st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span>].append({<span class=\&quot;hljs-string\&quot;>&amp;quot;role&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;assistant&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;content&amp;quot;</span>: ai_response})&quot;,&quot;        &quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> ai_response&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>except</span> Exception <span class=\&quot;hljs-keyword\&quot;>as</span> e:&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-string\&quot;>f&amp;quot;Error: <span class=\&quot;hljs-subst\&quot;>{e}</span>&amp;quot;</span>&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Define a function to generate a response from the Gemini 1.5 Pro model</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>generate_gemini_response</span>(<span class=\&quot;hljs-params\&quot;>prompt, file=<span class=\&quot;hljs-literal\&quot;>None</span>, file_type=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;        messages = [&quot;,&quot;            {<span class=\&quot;hljs-string\&quot;>&amp;quot;role&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;system&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;content&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;You are an AI assistant specializing in the circular economy. You provide insightful, practical, and innovative solutions to enhance sustainability and resource efficiency. You communicate in a clear and engaging manner, making complex topics easy to understand.&amp;quot;</span>},&quot;,&quot;            {<span class=\&quot;hljs-string\&quot;>&amp;quot;role&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;user&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;content&amp;quot;</span>: prompt},&quot;,&quot;        ]&quot;,&quot;        &quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> file <span class=\&quot;hljs-keyword\&quot;>and</span> file_type:&quot;,&quot;            messages.append({<span class=\&quot;hljs-string\&quot;>&amp;quot;role&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;user&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;content&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>f&amp;quot;Here is a <span class=\&quot;hljs-subst\&quot;>{file_type}</span> file for analysis.&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;file&amp;quot;</span>: file})&quot;,&quot;        &quot;,&quot;        response = openai.ChatCompletion.create(&quot;,&quot;            model=<span class=\&quot;hljs-string\&quot;>&amp;quot;gemini-1.5-pro&amp;quot;</span>,&quot;,&quot;            messages=messages&quot;,&quot;        )&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> response.choices[<span class=\&quot;hljs-number\&quot;>0</span>].message[<span class=\&quot;hljs-string\&quot;>&amp;#x27;content&amp;#x27;</span>]&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>except</span> Exception <span class=\&quot;hljs-keyword\&quot;>as</span> e:&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-string\&quot;>f&amp;quot;Error: <span class=\&quot;hljs-subst\&quot;>{e}</span>&amp;quot;</span>&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Function to simulate real-time data</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>get_real_time_data</span>():&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># Simulate real-time data for waste management</span>&quot;,&quot;    data = {&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;#x27;Time&amp;#x27;</span>: pd.date_range(start=<span class=\&quot;hljs-string\&quot;>&amp;#x27;2024-09-14 10:00&amp;#x27;</span>, periods=<span class=\&quot;hljs-number\&quot;>10</span>, freq=<span class=\&quot;hljs-string\&quot;>&amp;#x27;T&amp;#x27;</span>),&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;#x27;Waste Generated (kg)&amp;#x27;</span>: np.random.randint(<span class=\&quot;hljs-number\&quot;>50</span>, <span class=\&quot;hljs-number\&quot;>100</span>, size=<span class=\&quot;hljs-number\&quot;>10</span>)&quot;,&quot;    }&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> pd.DataFrame(data)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>get_circular_economy_locations</span>():&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># Simulate data for circular economy initiatives</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> pd.DataFrame({&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;#x27;name&amp;#x27;</span>: [<span class=\&quot;hljs-string\&quot;>&amp;#x27;Recycling Center&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Repair Cafe&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Upcycling Workshop&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Zero Waste Store&amp;#x27;</span>],&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;#x27;lat&amp;#x27;</span>: [<span class=\&quot;hljs-number\&quot;>40.7128</span>, <span class=\&quot;hljs-number\&quot;>34.0522</span>, <span class=\&quot;hljs-number\&quot;>51.5074</span>, <span class=\&quot;hljs-number\&quot;>48.8566</span>],&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;#x27;lon&amp;#x27;</span>: [-<span class=\&quot;hljs-number\&quot;>74.0060</span>, -<span class=\&quot;hljs-number\&quot;>118.2437</span>, -<span class=\&quot;hljs-number\&quot;>0.1278</span>, <span class=\&quot;hljs-number\&quot;>2.3522</span>],&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;#x27;type&amp;#x27;</span>: [<span class=\&quot;hljs-string\&quot;>&amp;#x27;Recycling&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Repair&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Upcycling&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Retail&amp;#x27;</span>]&quot;,&quot;    })&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>create_wordcloud</span>(<span class=\&quot;hljs-params\&quot;>text</span>):&quot;,&quot;    wordcloud = WordCloud(width=<span class=\&quot;hljs-number\&quot;>800</span>, height=<span class=\&quot;hljs-number\&quot;>400</span>, background_color=<span class=\&quot;hljs-string\&quot;>&amp;#x27;white&amp;#x27;</span>).generate(text)&quot;,&quot;    fig, ax = plt.subplots(figsize=(<span class=\&quot;hljs-number\&quot;>10</span>, <span class=\&quot;hljs-number\&quot;>5</span>))&quot;,&quot;    ax.imshow(wordcloud, interpolation=<span class=\&quot;hljs-string\&quot;>&amp;#x27;bilinear&amp;#x27;</span>)&quot;,&quot;    ax.axis(<span class=\&quot;hljs-string\&quot;>&amp;#x27;off&amp;#x27;</span>)&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> fig&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Set page config</span>&quot;,&quot;st.set_page_config(page_title=<span class=\&quot;hljs-string\&quot;>&amp;quot;Circular Economy Facilitator&amp;quot;</span>, page_icon=<span class=\&quot;hljs-string\&quot;>&amp;quot;♻️&amp;quot;</span>, layout=<span class=\&quot;hljs-string\&quot;>&amp;quot;wide&amp;quot;</span>)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Custom CSS (expanded)</span>&quot;,&quot;st.markdown(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;lt;style&amp;gt;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    .stApp {</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        background-color: #f0f8ff;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    }</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    .stHeader {</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        background-color: #4682b4;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    }</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    .stButton&amp;gt;button {</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        background-color: #4682b4;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        color: white;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        border-radius: 20px;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        padding: 10px 20px;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        transition: all 0.3s ease;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    }</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    .stButton&amp;gt;button:hover {</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        background-color: #36648b;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    }</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    .stTextInput&amp;gt;div&amp;gt;div&amp;gt;input {</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        background-color: #ffffff;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        border-radius: 10px;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    }</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    .stAlert {</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        background-color: #e6f3ff;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        border-left-color: #4682b4;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    }</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    .css-1d391kg {</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        padding-top: 3rem;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    }</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;lt;/style&amp;gt;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>, unsafe_allow_html=<span class=\&quot;hljs-literal\&quot;>True</span>)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Sidebar</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>with</span> st.sidebar:&quot;,&quot;    selected = option_menu(&quot;,&quot;        menu_title=<span class=\&quot;hljs-string\&quot;>&amp;quot;Navigation&amp;quot;</span>,&quot;,&quot;        options=[<span class=\&quot;hljs-string\&quot;>&amp;quot;Home&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Chat&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Data Analysis&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Resource Map&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Image Recognition&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Video Analysis&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Audio Processing&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Sustainability Quiz&amp;quot;</span>],&quot;,&quot;        icons=[<span class=\&quot;hljs-string\&quot;>&amp;quot;house&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;chat-dots&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;graph-up&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;geo-alt&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;image&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;camera-video&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;mic&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;question-circle&amp;quot;</span>],&quot;,&quot;        menu_icon=<span class=\&quot;hljs-string\&quot;>&amp;quot;cast&amp;quot;</span>,&quot;,&quot;        default_index=<span class=\&quot;hljs-number\&quot;>0</span>,&quot;,&quot;    )&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Main content</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>if</span> selected == <span class=\&quot;hljs-string\&quot;>&amp;quot;Home&amp;quot;</span>:&quot;,&quot;    st.title(<span class=\&quot;hljs-string\&quot;>&amp;quot;🌍 EcoSphere&amp;quot;</span>)&quot;,&quot;    st.write(<span class=\&quot;hljs-string\&quot;>&amp;quot;Welcome to EcoShpere! This app helps you explore sustainable practices, analyze data, and get AI-powered insights on various aspects of the circular economy.&amp;quot;</span>)&quot;,&quot;    &quot;,&quot;    col1, col2 = st.columns(<span class=\&quot;hljs-number\&quot;>2</span>)&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>with</span> col1:&quot;,&quot;        st.image(<span class=\&quot;hljs-string\&quot;>&amp;quot;https://via.placeholder.com/600x300.png?text=Circular+Economy+Concept&amp;quot;</span>, caption=<span class=\&quot;hljs-string\&quot;>&amp;quot;Circular Economy Concept&amp;quot;</span>, use_column_width=<span class=\&quot;hljs-literal\&quot;>True</span>)&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>with</span> col2:&quot;,&quot;        st.subheader(<span class=\&quot;hljs-string\&quot;>&amp;quot;Quick Tips for Sustainability&amp;quot;</span>)&quot;,&quot;        st.markdown(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        - Reduce, Reuse, Recycle</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        - Choose products with minimal packaging</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        - Support local and sustainable businesses</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        - Compost organic waste</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        - Use energy-efficient appliances</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        &amp;quot;&amp;quot;&amp;quot;</span>)&quot;,&quot;    &quot;,&quot;    st.subheader(<span class=\&quot;hljs-string\&quot;>&amp;quot;Latest Circular Economy News&amp;quot;</span>)&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># In a real app, you&amp;#x27;d fetch this data from a news API</span>&quot;,&quot;    st.markdown(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    1. [New Recycling Technology Breakthrough](https://example.com)</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    2. [Global Initiative to Reduce Plastic Waste](https://example.com)</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    3. [Circular Economy Creates New Job Opportunities](https://example.com)</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>elif</span> selected == <span class=\&quot;hljs-string\&quot;>&amp;quot;Chat&amp;quot;</span>:&quot;,&quot;    st.header(<span class=\&quot;hljs-string\&quot;>&amp;quot;💬 Chat with AI Assistant&amp;quot;</span>)&quot;,&quot;    &quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># Display conversation history</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>for</span> message <span class=\&quot;hljs-keyword\&quot;>in</span> st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span>]:&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> message[<span class=\&quot;hljs-string\&quot;>&amp;#x27;role&amp;#x27;</span>] != <span class=\&quot;hljs-string\&quot;>&amp;#x27;system&amp;#x27;</span>:&quot;,&quot;            st.chat_message(message[<span class=\&quot;hljs-string\&quot;>&amp;#x27;role&amp;#x27;</span>]).write(message[<span class=\&quot;hljs-string\&quot;>&amp;#x27;content&amp;#x27;</span>])&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># User input for prompt</span>&quot;,&quot;    user_input = st.chat_input(<span class=\&quot;hljs-string\&quot;>&amp;quot;Ask about circular economy concepts:&amp;quot;</span>)&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> user_input:&quot;,&quot;        st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span>].append({<span class=\&quot;hljs-string\&quot;>&amp;quot;role&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;user&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;content&amp;quot;</span>: user_input})&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>with</span> st.spinner(<span class=\&quot;hljs-string\&quot;>&amp;quot;Generating response...&amp;quot;</span>):&quot;,&quot;            ai_response = generate_response(user_input)&quot;,&quot;        st.chat_message(<span class=\&quot;hljs-string\&quot;>&amp;quot;assistant&amp;quot;</span>).write(ai_response)&quot;,&quot;        &quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Generate and display word cloud</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-built_in\&quot;>len</span>(st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span>]) &amp;gt; <span class=\&quot;hljs-number\&quot;>2</span>:&quot;,&quot;            all_text = <span class=\&quot;hljs-string\&quot;>&amp;quot; &amp;quot;</span>.join([m[<span class=\&quot;hljs-string\&quot;>&amp;#x27;content&amp;#x27;</span>] <span class=\&quot;hljs-keyword\&quot;>for</span> m <span class=\&quot;hljs-keyword\&quot;>in</span> st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;messages&amp;#x27;</span>] <span class=\&quot;hljs-keyword\&quot;>if</span> m[<span class=\&quot;hljs-string\&quot;>&amp;#x27;role&amp;#x27;</span>] != <span class=\&quot;hljs-string\&quot;>&amp;#x27;system&amp;#x27;</span>])&quot;,&quot;            st.subheader(<span class=\&quot;hljs-string\&quot;>&amp;quot;Conversation Topics&amp;quot;</span>)&quot;,&quot;            st.pyplot(create_wordcloud(all_text))&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>elif</span> selected == <span class=\&quot;hljs-string\&quot;>&amp;quot;Data Analysis&amp;quot;</span>:&quot;,&quot;    st.header(<span class=\&quot;hljs-string\&quot;>&amp;quot;📊 Real-Time Waste Management Data&amp;quot;</span>)&quot;,&quot;    &quot;,&quot;    col1, col2 = st.columns([<span class=\&quot;hljs-number\&quot;>3</span>, <span class=\&quot;hljs-number\&quot;>1</span>])&quot;,&quot;    &quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>with</span> col1:&quot;,&quot;        data = get_real_time_data()&quot;,&quot;        fig = px.line(data, x=<span class=\&quot;hljs-string\&quot;>&amp;#x27;Time&amp;#x27;</span>, y=<span class=\&quot;hljs-string\&quot;>&amp;#x27;Waste Generated (kg)&amp;#x27;</span>, title=<span class=\&quot;hljs-string\&quot;>&amp;#x27;Waste Generation Over Time&amp;#x27;</span>)&quot;,&quot;        st.plotly_chart(fig, use_container_width=<span class=\&quot;hljs-literal\&quot;>True</span>)&quot;,&quot;    &quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>with</span> col2:&quot;,&quot;        st.metric(<span class=\&quot;hljs-string\&quot;>&amp;quot;Total Waste&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>f&amp;quot;<span class=\&quot;hljs-subst\&quot;>{data[<span class=\&quot;hljs-string\&quot;>&amp;#x27;Waste Generated (kg)&amp;#x27;</span>].<span class=\&quot;hljs-built_in\&quot;>sum</span>()}</span> kg&amp;quot;</span>)&quot;,&quot;        st.metric(<span class=\&quot;hljs-string\&quot;>&amp;quot;Average Waste/min&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>f&amp;quot;<span class=\&quot;hljs-subst\&quot;>{data[<span class=\&quot;hljs-string\&quot;>&amp;#x27;Waste Generated (kg)&amp;#x27;</span>].mean():<span class=\&quot;hljs-number\&quot;>.2</span>f}</span> kg&amp;quot;</span>)&quot;,&quot;        st.metric(<span class=\&quot;hljs-string\&quot;>&amp;quot;Peak Waste&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>f&amp;quot;<span class=\&quot;hljs-subst\&quot;>{data[<span class=\&quot;hljs-string\&quot;>&amp;#x27;Waste Generated (kg)&amp;#x27;</span>].<span class=\&quot;hljs-built_in\&quot;>max</span>()}</span> kg&amp;quot;</span>)&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> st.button(<span class=\&quot;hljs-string\&quot;>&amp;quot;Analyze Data&amp;quot;</span>):&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>with</span> st.spinner(<span class=\&quot;hljs-string\&quot;>&amp;quot;Analyzing data...&amp;quot;</span>):&quot;,&quot;            prompt = <span class=\&quot;hljs-string\&quot;>&amp;quot;Analyze the following waste management data and provide insights on how to reduce waste and improve sustainability:\\n&amp;quot;</span> + data.to_string()&quot;,&quot;            ai_response = generate_gemini_response(prompt)&quot;,&quot;        st.info(<span class=\&quot;hljs-string\&quot;>&amp;quot;AI Assistant Insights&amp;quot;</span>)&quot;,&quot;        st.write(ai_response)&quot;,&quot;        &quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># Add a section for waste composition</span>&quot;,&quot;    st.subheader(<span class=\&quot;hljs-string\&quot;>&amp;quot;Waste Composition&amp;quot;</span>)&quot;,&quot;    waste_types = [<span class=\&quot;hljs-string\&quot;>&amp;#x27;Organic&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Plastic&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Paper&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Metal&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Glass&amp;#x27;</span>, <span class=\&quot;hljs-string\&quot;>&amp;#x27;Other&amp;#x27;</span>]&quot;,&quot;    waste_percentages = np.random.randint(<span class=\&quot;hljs-number\&quot;>10</span>, <span class=\&quot;hljs-number\&quot;>30</span>, size=<span class=\&quot;hljs-built_in\&quot;>len</span>(waste_types))&quot;,&quot;    waste_percentages = waste_percentages / waste_percentages.<span class=\&quot;hljs-built_in\&quot;>sum</span>() * <span class=\&quot;hljs-number\&quot;>100</span>&quot;,&quot;    &quot;,&quot;    fig = px.pie(values=waste_percentages, names=waste_types, title=<span class=\&quot;hljs-string\&quot;>&amp;#x27;Waste Composition&amp;#x27;</span>)&quot;,&quot;    st.plotly_chart(fig, use_container_width=<span class=\&quot;hljs-literal\&quot;>True</span>)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>elif</span> selected == <span class=\&quot;hljs-string\&quot;>&amp;quot;Resource Map&amp;quot;</span>:&quot;,&quot;    st.header(<span class=\&quot;hljs-string\&quot;>&amp;quot;🗺️ Circular Economy Resource Map&amp;quot;</span>)&quot;,&quot;    &quot;,&quot;    locations = get_circular_economy_locations()&quot;,&quot;    &quot;,&quot;    m = folium.Map(location=[<span class=\&quot;hljs-number\&quot;>40.7128</span>, -<span class=\&quot;hljs-number\&quot;>74.0060</span>], zoom_start=<span class=\&quot;hljs-number\&quot;>4</span>)&quot;,&quot;    &quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>for</span> _, row <span class=\&quot;hljs-keyword\&quot;>in</span> locations.iterrows():&quot;,&quot;        folium.Marker(&quot;,&quot;            location=[row[<span class=\&quot;hljs-string\&quot;>&amp;#x27;lat&amp;#x27;</span>], row[<span class=\&quot;hljs-string\&quot;>&amp;#x27;lon&amp;#x27;</span>]],&quot;,&quot;            popup=row[<span class=\&quot;hljs-string\&quot;>&amp;#x27;name&amp;#x27;</span>],&quot;,&quot;            tooltip=row[<span class=\&quot;hljs-string\&quot;>&amp;#x27;type&amp;#x27;</span>],&quot;,&quot;        ).add_to(m)&quot;,&quot;    &quot;,&quot;    folium_static(m)&quot;,&quot;    &quot;,&quot;    st.subheader(<span class=\&quot;hljs-string\&quot;>&amp;quot;Resource List&amp;quot;</span>)&quot;,&quot;    st.dataframe(locations)&quot;,&quot;    &quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> st.button(<span class=\&quot;hljs-string\&quot;>&amp;quot;Add Resource&amp;quot;</span>):&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>with</span> st.form(<span class=\&quot;hljs-string\&quot;>&amp;quot;add_resource&amp;quot;</span>):&quot;,&quot;            name = st.text_input(<span class=\&quot;hljs-string\&quot;>&amp;quot;Resource Name&amp;quot;</span>)&quot;,&quot;            resource_type = st.selectbox(<span class=\&quot;hljs-string\&quot;>&amp;quot;Resource Type&amp;quot;</span>, [<span class=\&quot;hljs-string\&quot;>&amp;quot;Recycling&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Repair&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Upcycling&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Retail&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Other&amp;quot;</span>])&quot;,&quot;            lat = st.number_input(<span class=\&quot;hljs-string\&quot;>&amp;quot;Latitude&amp;quot;</span>, min_value=-<span class=\&quot;hljs-number\&quot;>90.0</span>, max_value=<span class=\&quot;hljs-number\&quot;>90.0</span>)&quot;,&quot;            lon = st.number_input(<span class=\&quot;hljs-string\&quot;>&amp;quot;Longitude&amp;quot;</span>, min_value=-<span class=\&quot;hljs-number\&quot;>180.0</span>, max_value=<span class=\&quot;hljs-number\&quot;>180.0</span>)&quot;,&quot;            &quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> st.form_submit_button(<span class=\&quot;hljs-string\&quot;>&amp;quot;Submit&amp;quot;</span>):&quot;,&quot;                new_resource = pd.DataFrame({<span class=\&quot;hljs-string\&quot;>&amp;#x27;name&amp;#x27;</span>: [name], <span class=\&quot;hljs-string\&quot;>&amp;#x27;lat&amp;#x27;</span>: [lat], <span class=\&quot;hljs-string\&quot;>&amp;#x27;lon&amp;#x27;</span>: [lon], <span class=\&quot;hljs-string\&quot;>&amp;#x27;type&amp;#x27;</span>: [resource_type]})&quot;,&quot;                st.session_state[<span class=\&quot;hljs-string\&quot;>&amp;#x27;resources&amp;#x27;</span>] = pd.concat([locations, new_resource], ignore_index=<span class=\&quot;hljs-literal\&quot;>True</span>)&quot;,&quot;                st.success(<span class=\&quot;hljs-string\&quot;>&amp;quot;Resource added successfully!&amp;quot;</span>)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>elif</span> selected == <span class=\&quot;hljs-string\&quot;>&amp;quot;Image Recognition&amp;quot;</span>:&quot;,&quot;    st.header(<span class=\&quot;hljs-string\&quot;>&amp;quot;🖼️ Image Recognition&amp;quot;</span>)&quot;,&quot;    uploaded_image = st.file_uploader(<span class=\&quot;hljs-string\&quot;>&amp;quot;Upload an image for analysis&amp;quot;</span>, <span class=\&quot;hljs-built_in\&quot;>type</span>=[<span class=\&quot;hljs-string\&quot;>&amp;quot;jpg&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;png&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;jpeg&amp;quot;</span>])&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> uploaded_image:&quot;,&quot;        col1, col2 = st.columns(<span class=\&quot;hljs-number\&quot;>2</span>)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>with</span> col1:&quot;,&quot;            st.image(uploaded_image, caption=<span class=\&quot;hljs-string\&quot;>&amp;quot;Uploaded Image&amp;quot;</span>, use_column_width=<span class=\&quot;hljs-literal\&quot;>True</span>)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>with</span> col2:&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>with</span> st.spinner(<span class=\&quot;hljs-string\&quot;>&amp;quot;Analyzing image...&amp;quot;</span>):&quot;,&quot;                prompt = <span class=\&quot;hljs-string\&quot;>&amp;quot;Analyze this image to identify types of waste and suggest recycling or disposal methods.&amp;quot;</span>&quot;,&quot;                ai_response = generate_gemini_response(prompt, file=uploaded_image, file_type=<span class=\&quot;hljs-string\&quot;>&amp;quot;image&amp;quot;</span>)&quot;,&quot;            st.info(<span class=\&quot;hljs-string\&quot;>&amp;quot;AI Assistant Insights&amp;quot;</span>)&quot;,&quot;            st.write(ai_response)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>elif</span> selected == <span class=\&quot;hljs-string\&quot;>&amp;quot;Video Analysis&amp;quot;</span>:&quot;,&quot;    st.header(<span class=\&quot;hljs-string\&quot;>&amp;quot;🎥 Video Analysis&amp;quot;</span>)&quot;,&quot;    uploaded_video = st.file_uploader(<span class=\&quot;hljs-string\&quot;>&amp;quot;Upload a video for analysis&amp;quot;</span>, <span class=\&quot;hljs-built_in\&quot;>type</span>=[<span class=\&quot;hljs-string\&quot;>&amp;quot;mp4&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;mov&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;avi&amp;quot;</span>])&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> uploaded_video:&quot;,&quot;        st.video(uploaded_video)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>with</span> st.spinner(<span class=\&quot;hljs-string\&quot;>&amp;quot;Analyzing video...&amp;quot;</span>):&quot;,&quot;            prompt = <span class=\&quot;hljs-string\&quot;>&amp;quot;Analyze this video to identify sustainable practices and areas for improvement.&amp;quot;</span>&quot;,&quot;            ai_response = generate_gemini_response(prompt, file=uploaded_video, file_type=<span class=\&quot;hljs-string\&quot;>&amp;quot;video&amp;quot;</span>)&quot;,&quot;        st.info(<span class=\&quot;hljs-string\&quot;>&amp;quot;AI Assistant Insights&amp;quot;</span>)&quot;,&quot;        st.write(ai_response)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>elif</span> selected == <span class=\&quot;hljs-string\&quot;>&amp;quot;Audio Processing&amp;quot;</span>:&quot;,&quot;    st.header(<span class=\&quot;hljs-string\&quot;>&amp;quot;🎙️ Audio Processing&amp;quot;</span>)&quot;,&quot;    uploaded_audio = st.file_uploader(<span class=\&quot;hljs-string\&quot;>&amp;quot;Upload an audio file for analysis&amp;quot;</span>, <span class=\&quot;hljs-built_in\&quot;>type</span>=[<span class=\&quot;hljs-string\&quot;>&amp;quot;mp3&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;wav&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;m4a&amp;quot;</span>])&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> uploaded_audio:&quot;,&quot;        st.audio(uploaded_audio)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>with</span> st.spinner(<span class=\&quot;hljs-string\&quot;>&amp;quot;Analyzing audio...&amp;quot;</span>):&quot;,&quot;            prompt = <span class=\&quot;hljs-string\&quot;>&amp;quot;Analyze this audio to extract key points related to sustainability and resource efficiency.&amp;quot;</span>&quot;,&quot;            ai_response = generate_gemini_response(prompt, file=uploaded_audio, file_type=<span class=\&quot;hljs-string\&quot;>&amp;quot;audio&amp;quot;</span>)&quot;,&quot;        st.info(<span class=\&quot;hljs-string\&quot;>&amp;quot;AI Assistant Insights&amp;quot;</span>)&quot;,&quot;        st.write(ai_response)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>elif</span> selected == <span class=\&quot;hljs-string\&quot;>&amp;quot;Sustainability Quiz&amp;quot;</span>:&quot;,&quot;    st.header(<span class=\&quot;hljs-string\&quot;>&amp;quot;🧠 Sustainability Quiz&amp;quot;</span>)&quot;,&quot;    &quot;,&quot;    questions = [&quot;,&quot;        {&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;question&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;What is the primary goal of a circular economy?&amp;quot;</span>,&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;options&amp;quot;</span>: [<span class=\&quot;hljs-string\&quot;>&amp;quot;Maximize profits&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Eliminate all waste&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Keep resources in use for as long as possible&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Increase consumption&amp;quot;</span>],&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;correct&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;Keep resources in use for as long as possible&amp;quot;</span>&quot;,&quot;        },&quot;,&quot;        {&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;question&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;Which of the following is NOT a principle of the circular economy?&amp;quot;</span>,&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;options&amp;quot;</span>: [<span class=\&quot;hljs-string\&quot;>&amp;quot;Design out waste and pollution&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Keep products and materials in use&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Regenerate natural systems&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Increase linear consumption&amp;quot;</span>],&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;correct&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;Increase linear consumption&amp;quot;</span>&quot;,&quot;        },&quot;,&quot;        {&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;question&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;What is &amp;#x27;upcycling&amp;#x27;?&amp;quot;</span>,&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;options&amp;quot;</span>: [<span class=\&quot;hljs-string\&quot;>&amp;quot;Recycling materials into lower-value products&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Converting waste into new materials of better quality or higher environmental value&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Throwing away used products&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;Buying new eco-friendly products&amp;quot;</span>],&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>&amp;quot;correct&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;Converting waste into new materials of better quality or higher environmental value&amp;quot;</span>&quot;,&quot;        }&quot;,&quot;    ]&quot;,&quot;    &quot;,&quot;    score = <span class=\&quot;hljs-number\&quot;>0</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>for</span> i, q <span class=\&quot;hljs-keyword\&quot;>in</span> <span class=\&quot;hljs-built_in\&quot;>enumerate</span>(questions):&quot;,&quot;        st.subheader(<span class=\&quot;hljs-string\&quot;>f&amp;quot;Question <span class=\&quot;hljs-subst\&quot;>{i+<span class=\&quot;hljs-number\&quot;>1</span>}</span>&amp;quot;</span>)&quot;,&quot;        st.write(q[<span class=\&quot;hljs-string\&quot;>&amp;quot;question&amp;quot;</span>])&quot;,&quot;        answer = st.radio(<span class=\&quot;hljs-string\&quot;>&amp;quot;Select your answer:&amp;quot;</span>, q[<span class=\&quot;hljs-string\&quot;>&amp;quot;options&amp;quot;</span>], key=<span class=\&quot;hljs-string\&quot;>f&amp;quot;q<span class=\&quot;hljs-subst\&quot;>{i}</span>&amp;quot;</span>)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> answer == q[<span class=\&quot;hljs-string\&quot;>&amp;quot;correct&amp;quot;</span>]:&quot;,&quot;            score += <span class=\&quot;hljs-number\&quot;>1</span>&quot;,&quot;    &quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> st.button(<span class=\&quot;hljs-string\&quot;>&amp;quot;Submit Quiz&amp;quot;</span>):&quot;,&quot;        st.success(<span class=\&quot;hljs-string\&quot;>f&amp;quot;You scored <span class=\&quot;hljs-subst\&quot;>{score}</span> out of <span class=\&quot;hljs-subst\&quot;>{<span class=\&quot;hljs-built_in\&quot;>len</span>(questions)}</span>!&amp;quot;</span>)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> score == <span class=\&quot;hljs-built_in\&quot;>len</span>(questions):&quot;,&quot;            st.balloons()&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># Footer</span>&quot;,&quot;st.markdown(<span class=\&quot;hljs-string\&quot;>&amp;quot;---&amp;quot;</span>)&quot;,&quot;col1, col2, col3 = st.columns(<span class=\&quot;hljs-number\&quot;>3</span>)&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>with</span> col1:&quot;,&quot;    st.markdown(<span class=\&quot;hljs-string\&quot;>&amp;quot;© 2024 Circular Economy Facilitator&amp;quot;</span>)&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>with</span> col2:&quot;,&quot;    st.markdown(<span class=\&quot;hljs-string\&quot;>&amp;quot;[Privacy Policy](https://example.com) | [Terms of Service](https://example.com)&amp;quot;</span>)&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>with</span> col3:&quot;,&quot;    st.markdown(<span class=\&quot;hljs-string\&quot;>&amp;quot;Built with ❤️ for a sustainable future&amp;quot;</span>)&quot;],&quot;lineSelectorClass&quot;:&quot;blob-line&quot;,&quot;context&quot;:{&quot;repo&quot;:{&quot;name&quot;:&quot;Vorxart/AI-Agent&quot;,&quot;type&quot;:&quot;space&quot;},&quot;revision&quot;:&quot;6a6b7cf67d822341e7a1cac651fe588d7d38321c&quot;,&quot;path&quot;:&quot;app.py&quot;}}">

<div class="relative text-sm"><div class="overflow-x-auto"><table class="min-w-full border-collapse font-mono"><tbody><tr class="" id="L1">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="1"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> streamlit <span class="hljs-keyword">as</span> st<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L2">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="2"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> openai<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L3">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="3"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> os<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L4">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="4"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> pandas <span class="hljs-keyword">as</span> pd<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L5">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="5"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> numpy <span class="hljs-keyword">as</span> np<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L6">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="6"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> matplotlib.pyplot <span class="hljs-keyword">as</span> plt<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L7">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="7"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> streamlit_option_menu <span class="hljs-keyword">import</span> option_menu<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L8">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="8"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> streamlit_folium <span class="hljs-keyword">import</span> folium_static<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L9">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="9"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> folium<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L10">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="10"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> plotly.express <span class="hljs-keyword">as</span> px<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L11">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="11"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> wordcloud <span class="hljs-keyword">import</span> WordCloud<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L12">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="12"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L13">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="13"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Set up OpenAI client</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L14">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="14"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->openai.api_key = os.getenv(<span class="hljs-string">&quot;AIML_API_KEY&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L15">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="15"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->openai.api_base = <span class="hljs-string">&quot;https://api.aimlapi.com&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L16">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="16"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L17">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="17"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Initialize session state variables</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L18">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="18"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">if</span> <span class="hljs-string">&#x27;messages&#x27;</span> <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> st.session_state:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L19">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="19"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.session_state[<span class="hljs-string">&#x27;messages&#x27;</span>] = [<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L20">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="20"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        {<span class="hljs-string">&quot;role&quot;</span>: <span class="hljs-string">&quot;system&quot;</span>, <span class="hljs-string">&quot;content&quot;</span>: <span class="hljs-string">&quot;You are an AI assistant specializing in the circular economy. You provide insightful, practical, and innovative solutions to enhance sustainability and resource efficiency. You communicate in a clear and engaging manner, making complex topics easy to understand.&quot;</span>}<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L21">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="21"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    ]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L22">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="22"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">if</span> <span class="hljs-string">&#x27;resources&#x27;</span> <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> st.session_state:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L23">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="23"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.session_state[<span class="hljs-string">&#x27;resources&#x27;</span>] = []<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L24">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="24"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L25">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="25"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Define functions (keep existing functions and add new ones)</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L26">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="26"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L27">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="27"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Define a function to generate a response from the AI</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L28">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="28"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">generate_response</span>(<span class="hljs-params">prompt, model=<span class="hljs-string">&quot;meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo&quot;</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L29">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="29"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L30">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="30"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Add user message to the conversation history</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L31">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="31"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.session_state[<span class="hljs-string">&#x27;messages&#x27;</span>].append({<span class="hljs-string">&quot;role&quot;</span>: <span class="hljs-string">&quot;user&quot;</span>, <span class="hljs-string">&quot;content&quot;</span>: prompt})<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L32">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="32"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L33">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="33"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Generate response from the AI</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L34">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="34"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        response = openai.ChatCompletion.create(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L35">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="35"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            model=model,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L36">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="36"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            messages=st.session_state[<span class="hljs-string">&#x27;messages&#x27;</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L37">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="37"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L38">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="38"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L39">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="39"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Extract the AI response</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L40">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="40"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        ai_response = response.choices[<span class="hljs-number">0</span>].message[<span class="hljs-string">&#x27;content&#x27;</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L41">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="41"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L42">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="42"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Add AI response to the conversation history</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L43">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="43"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.session_state[<span class="hljs-string">&#x27;messages&#x27;</span>].append({<span class="hljs-string">&quot;role&quot;</span>: <span class="hljs-string">&quot;assistant&quot;</span>, <span class="hljs-string">&quot;content&quot;</span>: ai_response})<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L44">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="44"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L45">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="45"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> ai_response<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L46">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="46"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">except</span> Exception <span class="hljs-keyword">as</span> e:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L47">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="47"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> <span class="hljs-string">f&quot;Error: <span class="hljs-subst">{e}</span>&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L48">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="48"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L49">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="49"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Define a function to generate a response from the Gemini 1.5 Pro model</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L50">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="50"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">generate_gemini_response</span>(<span class="hljs-params">prompt, file=<span class="hljs-literal">None</span>, file_type=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L51">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="51"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L52">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="52"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        messages = [<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L53">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="53"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            {<span class="hljs-string">&quot;role&quot;</span>: <span class="hljs-string">&quot;system&quot;</span>, <span class="hljs-string">&quot;content&quot;</span>: <span class="hljs-string">&quot;You are an AI assistant specializing in the circular economy. You provide insightful, practical, and innovative solutions to enhance sustainability and resource efficiency. You communicate in a clear and engaging manner, making complex topics easy to understand.&quot;</span>},<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L54">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="54"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            {<span class="hljs-string">&quot;role&quot;</span>: <span class="hljs-string">&quot;user&quot;</span>, <span class="hljs-string">&quot;content&quot;</span>: prompt},<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L55">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="55"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        ]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L56">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="56"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L57">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="57"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> file <span class="hljs-keyword">and</span> file_type:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L58">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="58"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            messages.append({<span class="hljs-string">&quot;role&quot;</span>: <span class="hljs-string">&quot;user&quot;</span>, <span class="hljs-string">&quot;content&quot;</span>: <span class="hljs-string">f&quot;Here is a <span class="hljs-subst">{file_type}</span> file for analysis.&quot;</span>, <span class="hljs-string">&quot;file&quot;</span>: file})<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L59">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="59"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L60">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="60"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        response = openai.ChatCompletion.create(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L61">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="61"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            model=<span class="hljs-string">&quot;gemini-1.5-pro&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L62">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="62"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            messages=messages<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L63">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="63"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L64">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="64"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> response.choices[<span class="hljs-number">0</span>].message[<span class="hljs-string">&#x27;content&#x27;</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L65">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="65"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">except</span> Exception <span class="hljs-keyword">as</span> e:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L66">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="66"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> <span class="hljs-string">f&quot;Error: <span class="hljs-subst">{e}</span>&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L67">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="67"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L68">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="68"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Function to simulate real-time data</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L69">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="69"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">get_real_time_data</span>():<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L70">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="70"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># Simulate real-time data for waste management</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L71">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="71"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    data = {<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L72">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="72"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&#x27;Time&#x27;</span>: pd.date_range(start=<span class="hljs-string">&#x27;2024-09-14 10:00&#x27;</span>, periods=<span class="hljs-number">10</span>, freq=<span class="hljs-string">&#x27;T&#x27;</span>),<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L73">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="73"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&#x27;Waste Generated (kg)&#x27;</span>: np.random.randint(<span class="hljs-number">50</span>, <span class="hljs-number">100</span>, size=<span class="hljs-number">10</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L74">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="74"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    }<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L75">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="75"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> pd.DataFrame(data)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L76">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="76"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L77">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="77"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">get_circular_economy_locations</span>():<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L78">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="78"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># Simulate data for circular economy initiatives</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L79">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="79"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> pd.DataFrame({<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L80">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="80"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&#x27;name&#x27;</span>: [<span class="hljs-string">&#x27;Recycling Center&#x27;</span>, <span class="hljs-string">&#x27;Repair Cafe&#x27;</span>, <span class="hljs-string">&#x27;Upcycling Workshop&#x27;</span>, <span class="hljs-string">&#x27;Zero Waste Store&#x27;</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L81">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="81"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&#x27;lat&#x27;</span>: [<span class="hljs-number">40.7128</span>, <span class="hljs-number">34.0522</span>, <span class="hljs-number">51.5074</span>, <span class="hljs-number">48.8566</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L82">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="82"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&#x27;lon&#x27;</span>: [-<span class="hljs-number">74.0060</span>, -<span class="hljs-number">118.2437</span>, -<span class="hljs-number">0.1278</span>, <span class="hljs-number">2.3522</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L83">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="83"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&#x27;type&#x27;</span>: [<span class="hljs-string">&#x27;Recycling&#x27;</span>, <span class="hljs-string">&#x27;Repair&#x27;</span>, <span class="hljs-string">&#x27;Upcycling&#x27;</span>, <span class="hljs-string">&#x27;Retail&#x27;</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L84">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="84"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    })<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L85">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="85"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L86">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="86"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">create_wordcloud</span>(<span class="hljs-params">text</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L87">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="87"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    wordcloud = WordCloud(width=<span class="hljs-number">800</span>, height=<span class="hljs-number">400</span>, background_color=<span class="hljs-string">&#x27;white&#x27;</span>).generate(text)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L88">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="88"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    fig, ax = plt.subplots(figsize=(<span class="hljs-number">10</span>, <span class="hljs-number">5</span>))<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L89">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="89"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    ax.imshow(wordcloud, interpolation=<span class="hljs-string">&#x27;bilinear&#x27;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L90">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="90"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    ax.axis(<span class="hljs-string">&#x27;off&#x27;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L91">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="91"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> fig<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L92">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="92"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L93">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="93"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Set page config</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L94">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="94"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->st.set_page_config(page_title=<span class="hljs-string">&quot;Circular Economy Facilitator&quot;</span>, page_icon=<span class="hljs-string">&quot;♻️&quot;</span>, layout=<span class="hljs-string">&quot;wide&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L95">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="95"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L96">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="96"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Custom CSS (expanded)</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L97">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="97"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->st.markdown(<span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L98">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="98"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &lt;style&gt;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L99">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="99"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    .stApp {</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L100">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="100"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        background-color: #f0f8ff;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L101">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="101"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    }</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L102">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="102"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    .stHeader {</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L103">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="103"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        background-color: #4682b4;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L104">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="104"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    }</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L105">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="105"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    .stButton&gt;button {</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L106">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="106"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        background-color: #4682b4;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L107">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="107"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        color: white;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L108">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="108"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        border-radius: 20px;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L109">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="109"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        padding: 10px 20px;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L110">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="110"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        transition: all 0.3s ease;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L111">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="111"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    }</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L112">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="112"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    .stButton&gt;button:hover {</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L113">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="113"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        background-color: #36648b;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L114">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="114"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L115">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="115"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    }</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L116">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="116"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    .stTextInput&gt;div&gt;div&gt;input {</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L117">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="117"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        background-color: #ffffff;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L118">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="118"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        border-radius: 10px;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L119">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="119"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    }</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L120">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="120"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    .stAlert {</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L121">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="121"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        background-color: #e6f3ff;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L122">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="122"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        border-left-color: #4682b4;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L123">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="123"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    }</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L124">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="124"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    .css-1d391kg {</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L125">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="125"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        padding-top: 3rem;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L126">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="126"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    }</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L127">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="127"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &lt;/style&gt;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L128">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="128"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span>, unsafe_allow_html=<span class="hljs-literal">True</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L129">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="129"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L130">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="130"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Sidebar</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L131">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="131"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">with</span> st.sidebar:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L132">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="132"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    selected = option_menu(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L133">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="133"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        menu_title=<span class="hljs-string">&quot;Navigation&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L134">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="134"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        options=[<span class="hljs-string">&quot;Home&quot;</span>, <span class="hljs-string">&quot;Chat&quot;</span>, <span class="hljs-string">&quot;Data Analysis&quot;</span>, <span class="hljs-string">&quot;Resource Map&quot;</span>, <span class="hljs-string">&quot;Image Recognition&quot;</span>, <span class="hljs-string">&quot;Video Analysis&quot;</span>, <span class="hljs-string">&quot;Audio Processing&quot;</span>, <span class="hljs-string">&quot;Sustainability Quiz&quot;</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L135">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="135"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        icons=[<span class="hljs-string">&quot;house&quot;</span>, <span class="hljs-string">&quot;chat-dots&quot;</span>, <span class="hljs-string">&quot;graph-up&quot;</span>, <span class="hljs-string">&quot;geo-alt&quot;</span>, <span class="hljs-string">&quot;image&quot;</span>, <span class="hljs-string">&quot;camera-video&quot;</span>, <span class="hljs-string">&quot;mic&quot;</span>, <span class="hljs-string">&quot;question-circle&quot;</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L136">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="136"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        menu_icon=<span class="hljs-string">&quot;cast&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L137">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="137"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        default_index=<span class="hljs-number">0</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L138">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="138"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    )<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L139">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="139"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L140">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="140"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Main content</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L141">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="141"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">if</span> selected == <span class="hljs-string">&quot;Home&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L142">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="142"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.title(<span class="hljs-string">&quot;🌍 EcoSphere&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L143">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="143"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.write(<span class="hljs-string">&quot;Welcome to EcoShpere! This app helps you explore sustainable practices, analyze data, and get AI-powered insights on various aspects of the circular economy.&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L144">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="144"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L145">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="145"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    col1, col2 = st.columns(<span class="hljs-number">2</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L146">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="146"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">with</span> col1:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L147">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="147"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.image(<span class="hljs-string">&quot;https://via.placeholder.com/600x300.png?text=Circular+Economy+Concept&quot;</span>, caption=<span class="hljs-string">&quot;Circular Economy Concept&quot;</span>, use_column_width=<span class="hljs-literal">True</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L148">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="148"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">with</span> col2:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L149">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="149"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.subheader(<span class="hljs-string">&quot;Quick Tips for Sustainability&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L150">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="150"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.markdown(<span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L151">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="151"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        - Reduce, Reuse, Recycle</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L152">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="152"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        - Choose products with minimal packaging</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L153">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="153"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        - Support local and sustainable businesses</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L154">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="154"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        - Compost organic waste</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L155">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="155"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        - Use energy-efficient appliances</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L156">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="156"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        &quot;&quot;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L157">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="157"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L158">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="158"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.subheader(<span class="hljs-string">&quot;Latest Circular Economy News&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L159">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="159"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># In a real app, you&#x27;d fetch this data from a news API</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L160">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="160"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.markdown(<span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L161">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="161"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    1. [New Recycling Technology Breakthrough](https://example.com)</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L162">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="162"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    2. [Global Initiative to Reduce Plastic Waste](https://example.com)</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L163">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="163"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    3. [Circular Economy Creates New Job Opportunities](https://example.com)</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L164">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="164"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L165">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="165"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L166">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="166"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">elif</span> selected == <span class="hljs-string">&quot;Chat&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L167">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="167"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.header(<span class="hljs-string">&quot;💬 Chat with AI Assistant&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L168">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="168"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L169">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="169"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># Display conversation history</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L170">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="170"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">for</span> message <span class="hljs-keyword">in</span> st.session_state[<span class="hljs-string">&#x27;messages&#x27;</span>]:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L171">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="171"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> message[<span class="hljs-string">&#x27;role&#x27;</span>] != <span class="hljs-string">&#x27;system&#x27;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L172">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="172"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            st.chat_message(message[<span class="hljs-string">&#x27;role&#x27;</span>]).write(message[<span class="hljs-string">&#x27;content&#x27;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L173">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="173"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L174">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="174"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># User input for prompt</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L175">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="175"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    user_input = st.chat_input(<span class="hljs-string">&quot;Ask about circular economy concepts:&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L176">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="176"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L177">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="177"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> user_input:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L178">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="178"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.session_state[<span class="hljs-string">&#x27;messages&#x27;</span>].append({<span class="hljs-string">&quot;role&quot;</span>: <span class="hljs-string">&quot;user&quot;</span>, <span class="hljs-string">&quot;content&quot;</span>: user_input})<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L179">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="179"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">with</span> st.spinner(<span class="hljs-string">&quot;Generating response...&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L180">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="180"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            ai_response = generate_response(user_input)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L181">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="181"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.chat_message(<span class="hljs-string">&quot;assistant&quot;</span>).write(ai_response)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L182">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="182"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L183">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="183"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Generate and display word cloud</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L184">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="184"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(st.session_state[<span class="hljs-string">&#x27;messages&#x27;</span>]) &gt; <span class="hljs-number">2</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L185">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="185"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            all_text = <span class="hljs-string">&quot; &quot;</span>.join([m[<span class="hljs-string">&#x27;content&#x27;</span>] <span class="hljs-keyword">for</span> m <span class="hljs-keyword">in</span> st.session_state[<span class="hljs-string">&#x27;messages&#x27;</span>] <span class="hljs-keyword">if</span> m[<span class="hljs-string">&#x27;role&#x27;</span>] != <span class="hljs-string">&#x27;system&#x27;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L186">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="186"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            st.subheader(<span class="hljs-string">&quot;Conversation Topics&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L187">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="187"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            st.pyplot(create_wordcloud(all_text))<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L188">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="188"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L189">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="189"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">elif</span> selected == <span class="hljs-string">&quot;Data Analysis&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L190">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="190"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.header(<span class="hljs-string">&quot;📊 Real-Time Waste Management Data&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L191">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="191"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L192">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="192"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    col1, col2 = st.columns([<span class="hljs-number">3</span>, <span class="hljs-number">1</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L193">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="193"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L194">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="194"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">with</span> col1:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L195">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="195"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        data = get_real_time_data()<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L196">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="196"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        fig = px.line(data, x=<span class="hljs-string">&#x27;Time&#x27;</span>, y=<span class="hljs-string">&#x27;Waste Generated (kg)&#x27;</span>, title=<span class="hljs-string">&#x27;Waste Generation Over Time&#x27;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L197">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="197"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.plotly_chart(fig, use_container_width=<span class="hljs-literal">True</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L198">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="198"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L199">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="199"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">with</span> col2:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L200">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="200"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.metric(<span class="hljs-string">&quot;Total Waste&quot;</span>, <span class="hljs-string">f&quot;<span class="hljs-subst">{data[<span class="hljs-string">&#x27;Waste Generated (kg)&#x27;</span>].<span class="hljs-built_in">sum</span>()}</span> kg&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L201">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="201"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.metric(<span class="hljs-string">&quot;Average Waste/min&quot;</span>, <span class="hljs-string">f&quot;<span class="hljs-subst">{data[<span class="hljs-string">&#x27;Waste Generated (kg)&#x27;</span>].mean():<span class="hljs-number">.2</span>f}</span> kg&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L202">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="202"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.metric(<span class="hljs-string">&quot;Peak Waste&quot;</span>, <span class="hljs-string">f&quot;<span class="hljs-subst">{data[<span class="hljs-string">&#x27;Waste Generated (kg)&#x27;</span>].<span class="hljs-built_in">max</span>()}</span> kg&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L203">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="203"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L204">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="204"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> st.button(<span class="hljs-string">&quot;Analyze Data&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L205">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="205"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">with</span> st.spinner(<span class="hljs-string">&quot;Analyzing data...&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L206">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="206"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            prompt = <span class="hljs-string">&quot;Analyze the following waste management data and provide insights on how to reduce waste and improve sustainability:\n&quot;</span> + data.to_string()<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L207">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="207"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            ai_response = generate_gemini_response(prompt)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L208">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="208"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.info(<span class="hljs-string">&quot;AI Assistant Insights&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L209">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="209"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.write(ai_response)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L210">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="210"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L211">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="211"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># Add a section for waste composition</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L212">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="212"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.subheader(<span class="hljs-string">&quot;Waste Composition&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L213">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="213"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    waste_types = [<span class="hljs-string">&#x27;Organic&#x27;</span>, <span class="hljs-string">&#x27;Plastic&#x27;</span>, <span class="hljs-string">&#x27;Paper&#x27;</span>, <span class="hljs-string">&#x27;Metal&#x27;</span>, <span class="hljs-string">&#x27;Glass&#x27;</span>, <span class="hljs-string">&#x27;Other&#x27;</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L214">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="214"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    waste_percentages = np.random.randint(<span class="hljs-number">10</span>, <span class="hljs-number">30</span>, size=<span class="hljs-built_in">len</span>(waste_types))<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L215">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="215"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    waste_percentages = waste_percentages / waste_percentages.<span class="hljs-built_in">sum</span>() * <span class="hljs-number">100</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L216">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="216"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L217">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="217"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    fig = px.pie(values=waste_percentages, names=waste_types, title=<span class="hljs-string">&#x27;Waste Composition&#x27;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L218">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="218"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.plotly_chart(fig, use_container_width=<span class="hljs-literal">True</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L219">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="219"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L220">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="220"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">elif</span> selected == <span class="hljs-string">&quot;Resource Map&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L221">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="221"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.header(<span class="hljs-string">&quot;🗺️ Circular Economy Resource Map&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L222">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="222"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L223">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="223"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    locations = get_circular_economy_locations()<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L224">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="224"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L225">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="225"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    m = folium.Map(location=[<span class="hljs-number">40.7128</span>, -<span class="hljs-number">74.0060</span>], zoom_start=<span class="hljs-number">4</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L226">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="226"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L227">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="227"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">for</span> _, row <span class="hljs-keyword">in</span> locations.iterrows():<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L228">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="228"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        folium.Marker(<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L229">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="229"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            location=[row[<span class="hljs-string">&#x27;lat&#x27;</span>], row[<span class="hljs-string">&#x27;lon&#x27;</span>]],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L230">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="230"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            popup=row[<span class="hljs-string">&#x27;name&#x27;</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L231">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="231"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            tooltip=row[<span class="hljs-string">&#x27;type&#x27;</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L232">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="232"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        ).add_to(m)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L233">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="233"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L234">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="234"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    folium_static(m)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L235">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="235"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L236">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="236"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.subheader(<span class="hljs-string">&quot;Resource List&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L237">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="237"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.dataframe(locations)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L238">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="238"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L239">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="239"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> st.button(<span class="hljs-string">&quot;Add Resource&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L240">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="240"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">with</span> st.form(<span class="hljs-string">&quot;add_resource&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L241">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="241"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            name = st.text_input(<span class="hljs-string">&quot;Resource Name&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L242">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="242"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            resource_type = st.selectbox(<span class="hljs-string">&quot;Resource Type&quot;</span>, [<span class="hljs-string">&quot;Recycling&quot;</span>, <span class="hljs-string">&quot;Repair&quot;</span>, <span class="hljs-string">&quot;Upcycling&quot;</span>, <span class="hljs-string">&quot;Retail&quot;</span>, <span class="hljs-string">&quot;Other&quot;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L243">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="243"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            lat = st.number_input(<span class="hljs-string">&quot;Latitude&quot;</span>, min_value=-<span class="hljs-number">90.0</span>, max_value=<span class="hljs-number">90.0</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L244">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="244"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            lon = st.number_input(<span class="hljs-string">&quot;Longitude&quot;</span>, min_value=-<span class="hljs-number">180.0</span>, max_value=<span class="hljs-number">180.0</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L245">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="245"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L246">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="246"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> st.form_submit_button(<span class="hljs-string">&quot;Submit&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L247">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="247"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                new_resource = pd.DataFrame({<span class="hljs-string">&#x27;name&#x27;</span>: [name], <span class="hljs-string">&#x27;lat&#x27;</span>: [lat], <span class="hljs-string">&#x27;lon&#x27;</span>: [lon], <span class="hljs-string">&#x27;type&#x27;</span>: [resource_type]})<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L248">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="248"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                st.session_state[<span class="hljs-string">&#x27;resources&#x27;</span>] = pd.concat([locations, new_resource], ignore_index=<span class="hljs-literal">True</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L249">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="249"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                st.success(<span class="hljs-string">&quot;Resource added successfully!&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L250">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="250"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L251">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="251"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">elif</span> selected == <span class="hljs-string">&quot;Image Recognition&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L252">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="252"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.header(<span class="hljs-string">&quot;🖼️ Image Recognition&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L253">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="253"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    uploaded_image = st.file_uploader(<span class="hljs-string">&quot;Upload an image for analysis&quot;</span>, <span class="hljs-built_in">type</span>=[<span class="hljs-string">&quot;jpg&quot;</span>, <span class="hljs-string">&quot;png&quot;</span>, <span class="hljs-string">&quot;jpeg&quot;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L254">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="254"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> uploaded_image:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L255">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="255"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        col1, col2 = st.columns(<span class="hljs-number">2</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L256">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="256"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">with</span> col1:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L257">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="257"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            st.image(uploaded_image, caption=<span class="hljs-string">&quot;Uploaded Image&quot;</span>, use_column_width=<span class="hljs-literal">True</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L258">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="258"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">with</span> col2:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L259">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="259"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-keyword">with</span> st.spinner(<span class="hljs-string">&quot;Analyzing image...&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L260">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="260"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                prompt = <span class="hljs-string">&quot;Analyze this image to identify types of waste and suggest recycling or disposal methods.&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L261">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="261"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->                ai_response = generate_gemini_response(prompt, file=uploaded_image, file_type=<span class="hljs-string">&quot;image&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L262">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="262"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            st.info(<span class="hljs-string">&quot;AI Assistant Insights&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L263">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="263"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            st.write(ai_response)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L264">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="264"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L265">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="265"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">elif</span> selected == <span class="hljs-string">&quot;Video Analysis&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L266">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="266"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.header(<span class="hljs-string">&quot;🎥 Video Analysis&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L267">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="267"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    uploaded_video = st.file_uploader(<span class="hljs-string">&quot;Upload a video for analysis&quot;</span>, <span class="hljs-built_in">type</span>=[<span class="hljs-string">&quot;mp4&quot;</span>, <span class="hljs-string">&quot;mov&quot;</span>, <span class="hljs-string">&quot;avi&quot;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L268">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="268"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> uploaded_video:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L269">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="269"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.video(uploaded_video)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L270">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="270"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">with</span> st.spinner(<span class="hljs-string">&quot;Analyzing video...&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L271">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="271"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            prompt = <span class="hljs-string">&quot;Analyze this video to identify sustainable practices and areas for improvement.&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L272">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="272"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            ai_response = generate_gemini_response(prompt, file=uploaded_video, file_type=<span class="hljs-string">&quot;video&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L273">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="273"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.info(<span class="hljs-string">&quot;AI Assistant Insights&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L274">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="274"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.write(ai_response)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L275">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="275"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L276">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="276"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">elif</span> selected == <span class="hljs-string">&quot;Audio Processing&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L277">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="277"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.header(<span class="hljs-string">&quot;🎙️ Audio Processing&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L278">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="278"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    uploaded_audio = st.file_uploader(<span class="hljs-string">&quot;Upload an audio file for analysis&quot;</span>, <span class="hljs-built_in">type</span>=[<span class="hljs-string">&quot;mp3&quot;</span>, <span class="hljs-string">&quot;wav&quot;</span>, <span class="hljs-string">&quot;m4a&quot;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L279">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="279"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> uploaded_audio:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L280">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="280"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.audio(uploaded_audio)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L281">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="281"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">with</span> st.spinner(<span class="hljs-string">&quot;Analyzing audio...&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L282">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="282"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            prompt = <span class="hljs-string">&quot;Analyze this audio to extract key points related to sustainability and resource efficiency.&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L283">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="283"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            ai_response = generate_gemini_response(prompt, file=uploaded_audio, file_type=<span class="hljs-string">&quot;audio&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L284">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="284"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.info(<span class="hljs-string">&quot;AI Assistant Insights&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L285">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="285"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.write(ai_response)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L286">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="286"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L287">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="287"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">elif</span> selected == <span class="hljs-string">&quot;Sustainability Quiz&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L288">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="288"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.header(<span class="hljs-string">&quot;🧠 Sustainability Quiz&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L289">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="289"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L290">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="290"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    questions = [<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L291">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="291"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        {<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L292">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="292"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;question&quot;</span>: <span class="hljs-string">&quot;What is the primary goal of a circular economy?&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L293">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="293"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;options&quot;</span>: [<span class="hljs-string">&quot;Maximize profits&quot;</span>, <span class="hljs-string">&quot;Eliminate all waste&quot;</span>, <span class="hljs-string">&quot;Keep resources in use for as long as possible&quot;</span>, <span class="hljs-string">&quot;Increase consumption&quot;</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L294">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="294"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;correct&quot;</span>: <span class="hljs-string">&quot;Keep resources in use for as long as possible&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L295">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="295"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        },<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L296">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="296"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        {<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L297">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="297"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;question&quot;</span>: <span class="hljs-string">&quot;Which of the following is NOT a principle of the circular economy?&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L298">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="298"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;options&quot;</span>: [<span class="hljs-string">&quot;Design out waste and pollution&quot;</span>, <span class="hljs-string">&quot;Keep products and materials in use&quot;</span>, <span class="hljs-string">&quot;Regenerate natural systems&quot;</span>, <span class="hljs-string">&quot;Increase linear consumption&quot;</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L299">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="299"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;correct&quot;</span>: <span class="hljs-string">&quot;Increase linear consumption&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L300">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="300"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        },<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L301">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="301"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        {<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L302">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="302"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;question&quot;</span>: <span class="hljs-string">&quot;What is &#x27;upcycling&#x27;?&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L303">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="303"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;options&quot;</span>: [<span class="hljs-string">&quot;Recycling materials into lower-value products&quot;</span>, <span class="hljs-string">&quot;Converting waste into new materials of better quality or higher environmental value&quot;</span>, <span class="hljs-string">&quot;Throwing away used products&quot;</span>, <span class="hljs-string">&quot;Buying new eco-friendly products&quot;</span>],<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L304">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="304"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-string">&quot;correct&quot;</span>: <span class="hljs-string">&quot;Converting waste into new materials of better quality or higher environmental value&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L305">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="305"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        }<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L306">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="306"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    ]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L307">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="307"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L308">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="308"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    score = <span class="hljs-number">0</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L309">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="309"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">for</span> i, q <span class="hljs-keyword">in</span> <span class="hljs-built_in">enumerate</span>(questions):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L310">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="310"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.subheader(<span class="hljs-string">f&quot;Question <span class="hljs-subst">{i+<span class="hljs-number">1</span>}</span>&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L311">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="311"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.write(q[<span class="hljs-string">&quot;question&quot;</span>])<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L312">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="312"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        answer = st.radio(<span class="hljs-string">&quot;Select your answer:&quot;</span>, q[<span class="hljs-string">&quot;options&quot;</span>], key=<span class="hljs-string">f&quot;q<span class="hljs-subst">{i}</span>&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L313">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="313"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> answer == q[<span class="hljs-string">&quot;correct&quot;</span>]:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L314">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="314"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            score += <span class="hljs-number">1</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L315">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="315"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L316">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="316"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> st.button(<span class="hljs-string">&quot;Submit Quiz&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L317">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="317"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        st.success(<span class="hljs-string">f&quot;You scored <span class="hljs-subst">{score}</span> out of <span class="hljs-subst">{<span class="hljs-built_in">len</span>(questions)}</span>!&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L318">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="318"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> score == <span class="hljs-built_in">len</span>(questions):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L319">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="319"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            st.balloons()<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L320">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="320"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L321">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="321"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># Footer</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L322">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="322"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->st.markdown(<span class="hljs-string">&quot;---&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L323">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="323"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->col1, col2, col3 = st.columns(<span class="hljs-number">3</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L324">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="324"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">with</span> col1:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L325">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="325"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.markdown(<span class="hljs-string">&quot;© 2024 Circular Economy Facilitator&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L326">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="326"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">with</span> col2:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L327">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="327"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.markdown(<span class="hljs-string">&quot;[Privacy Policy](https://example.com) | [Terms of Service](https://example.com)&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L328">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="328"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">with</span> col3:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L329">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="329"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    st.markdown(<span class="hljs-string">&quot;Built with ❤️ for a sustainable future&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr></tbody></table></div>
	</div></div></div></div></section></div></main>

	</div>

		<script>
			import("/front/build/kube-ea367ff/index.js");
			window.moonSha = "kube-ea367ff/";
		</script>

		<!-- Stripe -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://js.stripe.com/v3/";
				script.async = true;
				document.head.appendChild(script);
			}
		</script>
	</body>
</html>
