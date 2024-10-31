# Array Manipulation Service Protocol

This protocol defines the client-server communication contract for array manipulation operations, where the client INFORMS the server with what array operations to be performed by the server. The client can request one of the following services:

1. **Sorting an Array**
2. **Finding the Maximum Value in an Array**
3. **Finding the Minimum Value in an Array**
4. **Adding Two Arrays Element-wise**
5. **Multiplying Two Arrays Element-wise**

All requests are sent via **headers**, and elements must be **delimited** by a comma **`,`**.

---

## 1. Array Sorting

To sort an array, the client should format the header as follows:

```
sort[ONESPACE]arraysize[ONESPACE]arrayelements[LINEFEED]
```

- **If the server successfully sorted the Array, it must return the following header**:
  ```
  SORTED[LINEFEED]
  ```
  Followed by the sorted array.

- **In the case of invalid input, the server must reply with the following header**:
  ```
  INVALID[ONESPACE]INPUT[LINEFEED]
  ```

---

## 2. Finding the Maximum Value in an Array

To find the maximum value in an array, the client should format the header as follows:

```
max[ONESPACE]arraysize[ONESPACE]arrayelements[LINEFEED]
```

**Example**:
```
max 5 1,2,3,4,5\n
```

- **When the server successfully gets the max value, it must return:**:
  ```
  MAX[ONESPACE]maxvalue[LINEFEED]
  ```

  **Example**:
  ```
  MAX 5\n
  ```

- **In the case of invalid inputs or an error, the server's response shoyld be:**:
  ```
  INVALID[ONESPACE]INPUT[LINEFEED]
  ```

---

## 3. Finding the Minimum Value in an Array

Similarly to the max, if the client wants to find the minimum value in an array, it should format the header as follows:

```
min[ONESPACE]arraysize[ONESPACE]arrayelements[LINEFEED]
```

**Example**:
```
min 5 1,2,3,4,5\n
```

- **When successful, the server must return this header:**:
  ```
  MIN[ONESPACE]minvalue[LINEFEED]
  ```

  **Example**:
  ```
  MIN 1\n
  ```

- **Error Response (Invalid Input)**:
  ```
  INVALID[ONESPACE]INPUT[LINEFEED]
  ```

---

## 4. Adding Two Arrays

To compute the element-wise sum of two arrays, the client should format the header as follows:

```
add[ONESPACE]array1size[ONESPACE]array1elements[ONESPACE]array2size[ONESPACE]array2elements[LINEFEED]
```

**Example**:
```
add 5 1,2,3,4,5 5 6,7,8,9,10\n
```

- **Successful Response**:
  ```
  ADDED[LINEFEED]
  ```
Followed by the summed array
  
  **Example**:
  ```
  ADDED\n
  7,9,11,13,15
  ```

- **Error Response (Invalid Input)**:
  ```
  INVALID[ONESPACE]INPUT[LINEFEED]
  ```

---

## 5. Multiplying Two Arrays

To compute the element-wise product of two arrays, the client should format the header as follows:

```
multiply[ONESPACE]array1size[ONESPACE]array1elements[ONESPACE]array2size[ONESPACE]array2elements[LINEFEED]
```

**Example**:
```
multiply 5 1,2,3,4,5 5 6,7,8,9,10\n
```

- **Successful Response**:
  ```
  MULTIPLIED[LINEFEED]
  ```
followed by the multiplied elements' array
  
  **Example**:
  ```
  MULTIPLIED\n
  6,14,24,36,50
  ```

- **The servers' error response should be as the following**:
  ```
  INVALID[ONESPACE]INPUT[LINEFEED]
  ```
