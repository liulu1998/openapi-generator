# echo-api-native

Echo Server API

- API version: 0.1.0

Echo Server API


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*

## Requirements

Building the API client library requires:

1. Java 11+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>echo-api-native</artifactId>
  <version>0.1.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "org.openapitools:echo-api-native:0.1.0"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

- `target/echo-api-native-0.1.0.jar`
- `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

import org.openapitools.client.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.BodyApi;

public class BodyApiExample {

    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        // Configure clients using the `defaultClient` object, such as
        // overriding the host and port, timeout, etc.
        BodyApi apiInstance = new BodyApi(defaultClient);
        Pet pet = new Pet(); // Pet | Pet object that needs to be added to the store
        try {
            Pet result = apiInstance.testEchoBodyPet(pet);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BodyApi#testEchoBodyPet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:3000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BodyApi* | [**testEchoBodyPet**](docs/BodyApi.md#testEchoBodyPet) | **POST** /echo/body/Pet | Test body parameter(s)
*BodyApi* | [**testEchoBodyPetWithHttpInfo**](docs/BodyApi.md#testEchoBodyPetWithHttpInfo) | **POST** /echo/body/Pet | Test body parameter(s)
*PathApi* | [**testsPathStringPathStringIntegerPathInteger**](docs/PathApi.md#testsPathStringPathStringIntegerPathInteger) | **GET** /path/string/{path_string}/integer/{path_integer} | Test path parameter(s)
*PathApi* | [**testsPathStringPathStringIntegerPathIntegerWithHttpInfo**](docs/PathApi.md#testsPathStringPathStringIntegerPathIntegerWithHttpInfo) | **GET** /path/string/{path_string}/integer/{path_integer} | Test path parameter(s)
*QueryApi* | [**testQueryIntegerBooleanString**](docs/QueryApi.md#testQueryIntegerBooleanString) | **GET** /query/integer/boolean/string | Test query parameter(s)
*QueryApi* | [**testQueryIntegerBooleanStringWithHttpInfo**](docs/QueryApi.md#testQueryIntegerBooleanStringWithHttpInfo) | **GET** /query/integer/boolean/string | Test query parameter(s)
*QueryApi* | [**testQueryStyleFormExplodeTrueArrayString**](docs/QueryApi.md#testQueryStyleFormExplodeTrueArrayString) | **GET** /query/style_form/explode_true/array_string | Test query parameter(s)
*QueryApi* | [**testQueryStyleFormExplodeTrueArrayStringWithHttpInfo**](docs/QueryApi.md#testQueryStyleFormExplodeTrueArrayStringWithHttpInfo) | **GET** /query/style_form/explode_true/array_string | Test query parameter(s)
*QueryApi* | [**testQueryStyleFormExplodeTrueObject**](docs/QueryApi.md#testQueryStyleFormExplodeTrueObject) | **GET** /query/style_form/explode_true/object | Test query parameter(s)
*QueryApi* | [**testQueryStyleFormExplodeTrueObjectWithHttpInfo**](docs/QueryApi.md#testQueryStyleFormExplodeTrueObjectWithHttpInfo) | **GET** /query/style_form/explode_true/object | Test query parameter(s)


## Documentation for Models

 - [Category](docs/Category.md)
 - [Pet](docs/Pet.md)
 - [Tag](docs/Tag.md)
 - [TestQueryStyleFormExplodeTrueArrayStringQueryObjectParameter](docs/TestQueryStyleFormExplodeTrueArrayStringQueryObjectParameter.md)


## Documentation for Authorization

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.
However, the instances of the api clients created from the `ApiClient` are thread-safe and can be re-used.

## Author

team@openapitools.org

