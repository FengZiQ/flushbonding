# coding=utf-8
# 2019.01.08
import testlink
import time
import re


url = "http://192.168.20.94:8083/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
tester_key = {"admin": "68f26f458e8b1d537043f76d78f815d9"}
tlc = testlink.TestlinkAPIClient(url, tester_key["admin"])

project_name = '嵌入式固件'
test_plan_name = '固件网络配置'
first_menu = ['盒子', '国内立扫公版用例']


# 读取用例执行结果
def test_result():
    with open('testlinkNote', 'r', encoding='UTF-8', errors='ignore') as f:
        content = f.read()
        f.close()

    return content


# 更新测试结果
def to_execute_cases():

    # 获取本次要测试的项目
    projects = tlc.getProjects()
    target_project = [project for project in projects if project['name'] == project_name]

    # 获取本次执行的测试计划
    test_plan = tlc.getProjectTestPlans(target_project[0]['id'])
    target_test_plan = [plan for plan in test_plan if plan['active'] == '1' and test_plan_name in plan['name']]
    target_test_plan_id = target_test_plan[0]['id']

    # 获取本次要测试的所有用例
    target_test_cases = tlc.getTestCasesForTestPlan(target_test_plan[0]['id']).values()

    # 更新测试结果
    for case in target_test_cases:
        for case_body in case.values():
            # 判断测试用例是否更新结果：未执行或执行失败的用例需要被执行
            if not case_body['exec_on_build'] or case_body['exec_status'] == 'f':
                # 获取reportTCResult函数所需要的时间戳
                start_time = time.time()
                time_stamp = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                duration_min = str((time.time() - start_time)/60)

                # 获取reportTCResult函数所需要的其他信息
                case_id = case_body["tcase_id"]
                build_information = tlc.getBuildsForTestPlan(target_test_plan[0]['id'])
                build_name = build_information[0]["name"]
                test_case_external_id = case_body['external_id']
                case_platform_name = case_body['platform_name']

                # 在所有执行结果中找到目标用例的执行结果
                test_case_result = None
                steps_notes = None

                result = test_result()

                test_case_step_results = [
                    {
                        'step_number': 1,
                        'result': test_case_result,
                        'notes': steps_notes
                    }
                ]

                tlc.reportTCResult(
                    case_id, target_test_plan_id,
                    build_name,
                    test_case_result,
                    'automated test cases',
                    guess=True,
                    testcaseexternalid=test_case_external_id,
                    platformname=case_platform_name,
                    execduration=duration_min,
                    timestamp=time_stamp,
                    steps=test_case_step_results
                )


if __name__ == "__main__":
    to_execute_cases()
