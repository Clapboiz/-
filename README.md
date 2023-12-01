# Scientific research

## About web pentest
**Define reward:**

  * Gather new information
    
    * Learning about new marchine: 5 reward
    * Checking an exploit and learning it is valuable: 1 reward
    * Garthering loot provides 1 reward, 5 reward for password hashes
    
    **_=> This is only for new information and Garthering loot mean "loot" is valuable documents or information that an attacker can obtain from a compromised system_**

  * Successfully excuting vulnerablities:
    * Give 10 reward
    * Gaining superuser privileges (Admintrator): 20 reward

  * Movement fails: -1 reward

## Custom env
**_FlatActionSpace (Không Gian Hành Động Phẳng):_**

**Ý Nghĩa Trong Ngữ Cảnh Pentest:**
 
 **Mỗi hành động là một nhiệm vụ cụ thể mà một đại lý học tập có thể thực hiện.**
 
 _Ví Dụ:_
   
  * Hành động 1: "Khai thác lỗ hổng A"
  * Hành động 2: "Quét dịch vụ B"
  * Hành động 3: "Nâng cao đặc quyền"
  * Mỗi hành động tương ứng với một công việc cụ thể mà đại lý có thể chọn.

**_ParameterisedActionSpace (Không Gian Hành Động Tham Số Hóa):_**

**Ý Nghĩa Trong Ngữ Cảnh Pentest:**

**Mỗi hành động có thể được thực hiện với các tham số khác nhau, tạo ra nhiều biến thể của một loại hành động.**

_Ví Dụ:_

  * Hành động: "Khai thác lỗ hổng"
  * Tham số 1: Loại lỗ hổng (A, B, C)
  * Tham số 2: Mục tiêu (Máy chủ 1, Máy chủ 2)
  * Tham số 3: Cấp độ đặc quyền (User, Root)
    
Bằng cách này, đại lý có thể thực hiện hành động "Khai thác lỗ hổng" với nhiều biến thể khác nhau bằng cách thay đổi các tham số.

**Tại sao chỉ có 2 Action Spaces:**

**_Cung cấp hai không gian hành động này để phù hợp với sự đa dạng của các tác vụ và yêu cầu của việc học tập. Sự linh hoạt giúp mô hình đại lý học tập học được cách tương tác với môi trường và thực hiện các nhiệm vụ kiểm thử đánh sập một cách hiệu quả._**

## References
[1] _"Training an Autonomous Pentester with Deep RL" by Shane Caldwell. Link: "https://www.thestrangeloop.com/2021/training-an-autonomous-pentester-with-deep-rl.html"_
