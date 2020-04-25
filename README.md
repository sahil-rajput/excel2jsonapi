# excel2jsonapi

Convert EXCEL into API JSON Response.

Install Package
<pre>
pip install excel2jsonapi
</pre>


Excel Format
![img](https://user-images.githubusercontent.com/20112458/80275568-c352fe00-86ff-11ea-92b9-688fd6ad9a3c.png)


<pre>
>>> import excel2jsonapi
>>> excel2jsonapi.create('~/Desktop/excel2jsonapi/example/sample.xlsx')
</pre>

Response:
<pre>
[
   {
      "Name":"Rat",
      "Phone Number":"99999999",
      "Email":"rat@example.com"
   },
   {
      "Name":"Cat",
      "Phone Number":"88888888",
      "Email":"cat@example.com"
   },
   {
      "Name":"Dog",
      "Phone Number":"77777777",
      "Email":"dog@example.com"
   }
]
</pre>
