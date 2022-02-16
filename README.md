<div align="center">
	<a  href="https://www.storyblok.com?utm_source=github.com&utm_medium=readme&utm_campaign=storyblok-python-sdk"  align="center">
		<img  src="https://a.storyblok.com/f/88751/1776x360/f26fed5247/sb-python.png"  alt="Storyblok Logo">
	</a>
	<h1 align="center">Storyblok Python Client</h1>
	<p align="center">This is the official <a href="http://www.storyblok.com?utm_source=github.com&utm_medium=readme&utm_campaign=storyblok-python-sdk" target="_blank">Storyblok</a> client for Python.</p>
</div>

<p align="center">
  <a href="https://discord.gg/jKrbAMz">
   <img src="https://img.shields.io/discord/700316478792138842?label=Join%20Our%20Discord%20Community&style=appveyor&logo=discord&color=09b3af">
   </a>
  <a href="https://twitter.com/intent/follow?screen_name=storyblok">
    <img src="https://img.shields.io/badge/Follow-%40storyblok-09b3af?style=appveyor&logo=twitter" alt="Follow @Storyblok" />
  </a><br/>
  <a href="https://app.storyblok.com/#!/signup?utm_source=github.com&utm_medium=readme&utm_campaign=storyblok-python-sdk">
    <img src="https://img.shields.io/badge/Try%20Storyblok-Free-09b3af?style=appveyor&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABGdBTUEAALGPC/xhBQAAADhlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAAqACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADpiRU/AAACRElEQVRIDWNgGGmAEd3D3Js3LPrP8D8WXZwSPiMjw6qvPoHhyGYwIXNAbGpbCjbzP0MYuj0YFqMroBV/wCxmIeSju64eDNzMBJUxvP/9i2Hnq5cM1devMnz984eQsQwETeRhYWHgIcJiXqC6VHlFBjUeXgav40cIWkz1oLYXFmGwFBImaDFBHyObcOzdW4aSq5eRhRiE2dgYlpuYoYSKJi8vw3GgWnyAJIs/AuPu4scPGObd/fqVQZ+PHy7+6udPOBsXgySLDfn5GRYYmaKYJcXBgWLpsx8/GPa8foWiBhuHJIsl2DkYQqWksZkDFgP5PObcKYYff//iVAOTIDlx/QPqRMb/YSYBaWlOToZIaVkGZmAZSQiQ5OPtwHwacuo4iplMQEu6tXUZMhSUGDiYmBjylFQYvv/7x9B04xqKOnQOyT5GN+Df//8M59ASXKyMHLoyDD5JPtbj42OYrm+EYgg70JfuYuIoYmLs7AwMjIzA+uY/zjAnyWJpDk6GOFnCvrn86SOwmsNtKciVFAc1ileBHFDC67lzG10Yg0+SjzF0ownsf/OaofvOLYaDQJoQIGix94ljv1gIZI8Pv38zPvj2lQWYf3HGKbpDCFp85v07NnRN1OBTPY6JdRSGxcCw2k6sZuLVMZ5AV4s1TozPnGGFKbz+/PE7IJsHmC//MDMyhXBw8e6FyRFLv3Z0/IKuFqvFyIqAzd1PwBzJw8jAGPfVx38JshwlbIygxmYY43/GQmpais0ODDHuzevLMARHBcgIAQAbOJHZW0/EyQAAAABJRU5ErkJggg==" alt="Follow @Storyblok" />
  </a>
</p>

## 🚀 Usage

### Installation

Make sure you have [pip](https://pypi.python.org/pypi/pip) installed

```bash
$ pip install storyblok
```

###### Versions

Works with [ 2.6 / 2.7 / 3.2 / 3.3 ]

### Usage

```python
import storyblok

# Then we instantiate a client (as shown below)
```

#### Build a client

####### Without any authentication

```python
client = storyblok.Client()

# If you need to send options
client = storyblok.Client({}, client_options)
```

#### Client Options

The following options are available while instantiating a client:

 * __base__: Base url for the api
 * __api_version__: Default version of the api (to be used in url)
 * __user_agent__: Default user-agent for all requests
 * __headers__: Default headers for all requests
 * __request_type__: Default format of the request body

#### Response information

__All the callbacks provided to an api call will recieve the response as shown below__

```python
response = client.klass('args').method('args', method_options)

response.code
# >>> 200

response.headers
# >>> {'content-type': 'application/json; charset=utf-8'}
```

####### JSON response

When the response sent by server is __json__, it is decoded into a dict

```python
response.body
# >>> {"story": {"name":"story_name"}}
```

#### Method Options

The following options are available while calling a method of an api:

 * __api_version__: Version of the api (to be used in url)
 * __headers__: Headers for the request
 * __query__: Query parameters for the url
 * __body__: Body of the request
 * __request_type__: Format of the request body

#### Request body information

Set __request_type__ in options to modify the body accordingly

####### JSON request

When the value is set to __json__, JSON encode the body.

```python
body = {'story': {'name':"story_name"}}
# >>> '{"story": {"name":"story_name"}}'
```

#### Spaces api

Returns your current space name, published version and domain

```python
spaces = client.spaces()
```

####### Get current space (GET /cdn/spaces/me)

This endpoint is mostly useful for client side apps. The response contains space.version which you can use to call the story api and get the most recent published version. (https://www.storyblok.com/docs/Delivery-Api/spaces)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = spaces.me("your_access_token", options)
```

#### Stories api

Returns stories api instance

```python
stories = client.stories()
```

####### Get a list of stories (GET /cdn/stories/)

Returns a list of Stories (https://www.storyblok.com/docs/Delivery-Api/get-a-story#get-a-list-of-stories)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = stories.list("your_access_token", "draft", "1", "25", "posts", "1527067945", options)
```

####### Get a story by id (GET /cdn/stories/:story_id)

Returns a single story by id (https://www.storyblok.com/docs/Delivery-Api/get-a-story#get-a-story-by-id)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = stories.single("your_access_token", "draft", "41252", options)
```

#### Tags api

Returns tags api instance

```python
tags = client.tags()
```

####### Get a list of tags (GET /cdn/tags/)

Returns a list of tags (https://www.storyblok.com/docs/Delivery-Api/Tags)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = tags.list("your_access_token", "de", options)
```

#### Links api

Returns links api instance

```python
links = client.links()
```

####### Get a list of links (GET /cdn/links/)

Returns a list of links (https://www.storyblok.com/docs/Delivery-Api/Links)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = links.list("your_access_token", "draft", "de", options)
```

####### Get a link by id (GET /cdn/links/:id)

Returns a single link by id (https://www.storyblok.com/docs/Delivery-Api/Links#get-a-single-link)

The following arguments are required:

 * __token__: Public token for published or private token for draft version
 * __id__: Uuid of the link

```python
response = links.single("your_access_token", "148ee49a-ad81-4aff-b3d5-a2b4b6739e65", options)
```

#### Tags api

Returns tags api instance

```python
datasource_entries = client.datasource_entries()
```

####### Get a list of tags (GET /cdn/datasource_entries/)

Returns a list of tags (https://www.storyblok.com/docs/Delivery-Api/Tags)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = datasource_entries.list("your_access_token", "labels", "de-at", options)
```


## 🔗 Related Links

* **[Storyblok & Python on GitHub](https://github.com/search?q=org%3Astoryblok+topic%3Apython)**: Check all of our Python open source repos;
* **[Technology Hub](https://www.storyblok.com/technologies?utm_source=github.com&utm_medium=readme&utm_campaign=storyblok-python-sdk)**: We prepared technology hubs so that you can find selected beginner tutorials, videos, boilerplates, and even cheatsheets all in one place;
* **[Storyblok CLI](https://github.com/storyblok/storyblok)**: A simple CLI for scaffolding Storyblok projects and fieldtypes.

## ℹ️ More Resources

### Support

* Bugs or Feature Requests? [Submit an issue](../../../issues/new);

* Do you have questions about Storyblok or you need help? [Join our Discord Community](https://discord.gg/jKrbAMz).

### Contributing

Please see our [contributing guidelines](https://github.com/storyblok/.github/blob/master/contributing.md) and our [code of conduct](https://www.storyblok.com/trust-center#code-of-conduct?utm_source=github.com&utm_medium=readme&utm_campaign=storyblok-python-sdk).
This project use [semantic-release](https://semantic-release.gitbook.io/semantic-release/) for generate new versions by using commit messages and we use the Angular Convention to naming the commits. Check [this question](https://semantic-release.gitbook.io/semantic-release/support/faq#how-can-i-change-the-type-of-commits-that-trigger-a-release) about it in semantic-release FAQ.
