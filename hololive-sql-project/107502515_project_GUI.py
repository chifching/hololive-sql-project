import wx
import wx.grid
from mydb import Sql_operation
#創建hololive資料庫登入界面類別
class UserLogin(wx.Frame):
    #初始化登入界面
    def __init__(self, *args, **kw):
        #ensure the parent's __init__ is called
        super(UserLogin, self).__init__(*args, **kw)
        #設定framecentre
        self.Center()
        #創建panel
        self.pnl = wx.Panel(self)   
        #set Panel color
        self.pnl.SetBackgroundColour((0,255,196))
        #call登入界面func
        self.LoginInterface()
    def LoginInterface(self):
        #創建垂直box管理排版
        vbox = wx.BoxSizer(wx.VERTICAL)       
        #創建logo文字標籤
        logo = wx.StaticText(self.pnl, label="hololive資料庫")
        #set StaticText color
        logo.SetForegroundColour((0,200,255))
        logo.SetBackgroundColour((224,255,255))
        #set font attribute
        font = logo.GetFont()
        font.PointSize += 50
        font = font.Bold()
        logo.SetFont(font)
        #新增logo文字標籤到vbox管理排版        
        vbox.Add(logo, proportion=0, flag= wx.TOP )
        #創建靜態框
        sb_username = wx.StaticBox(self.pnl, label="帳號")
        sb_password = wx.StaticBox(self.pnl, label="密碼")
        #創建水平box管理排版
        hsbox_username = wx.StaticBoxSizer(sb_username, wx.HORIZONTAL)
        hsbox_password = wx.StaticBoxSizer(sb_password, wx.HORIZONTAL)
        #創建帳號、密碼輸入框
        self.user_name = wx.TextCtrl(self.pnl, size=(210, 25))
        self.user_password = wx.TextCtrl(self.pnl, size=(210, 25),style=wx.TE_PASSWORD)
        #新增帳號和密碼輸入框到hsbox管理排版
        hsbox_username.Add(self.user_name, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_password.Add(self.user_password, 0, wx.EXPAND | wx.BOTTOM, 5)
        #將水平box新增到垂直box
        vbox.Add(hsbox_username, proportion=0, flag=wx.CENTER)
        vbox.Add(hsbox_password, proportion=0, flag=wx.CENTER)
        #創建水平box管理排版
        hbox = wx.BoxSizer()
        #創建登入按鈕、綁定事件
        login_button = wx.Button(self.pnl, label="登入", size=(80, 25))
        login_button.Bind(wx.EVT_BUTTON, self.LoginButton)
        #新增登入按鈕到hbox管理排版
        hbox.Add(login_button, 0, flag=wx.EXPAND | wx.TOP, border=5)
        #將水平box新增到垂直box
        vbox.Add(hbox, proportion=0, flag=wx.CENTER)
        #設定面板的管理排版vbox
        self.pnl.SetSizer(vbox)
    def LoginButton(self, event):
        #連接holo_db資料庫
        op = Sql_operation("holo_db")
        #獲得users表中的帳號和密碼資訊，回傳tuple
        np = op.FindAll("users")
        #flag
        login_sign = 0
        #配對帳號和密碼
        for i in np:
            if (i[1] == self.user_name.GetValue()) and (i[2] == self.user_password.GetValue()):
                login_sign = 1
                break
        if login_sign == 0:
            print("帳號或密碼錯誤！")
            print(np)
        elif login_sign == 1:
            print("登入成功！")
            operation = UserOperation(None, title="hololive資料庫", size=(1024, 668))
            operation.Show()
            self.Close(True)
#操作界面
class UserOperation(wx.Frame):
    def __init__(self, *args, **kw):
        #ensure the parent's __init__ is called
        super(UserOperation, self).__init__(*args, **kw)
        #設定framecentre
        self.Center()
        #創建panel
        self.pnl = wx.Panel(self)
        #set Panel color
        self.pnl.SetBackgroundColour((0,255,196))
        #call操作界面func
        self.OperationInterface()

    def OperationInterface(self):
        #創建垂直box管理排版
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        #創建logo文字標籤
        logo = wx.StaticText(self.pnl, label="hololive資料庫")
        #set StaticText color
        logo.SetForegroundColour((0,200,255))
        logo.SetBackgroundColour((224,255,255))
        #set font attribute
        font = logo.GetFont()
        font.PointSize += 30
        font = font.Bold()
        logo.SetFont(font)
        #新增logo文字標籤到vbox管理排版
        self.vbox.Add(logo, proportion=0, flag=wx.FIXED_MINSIZE |
                      wx.TOP | wx.CENTER, border=5)
        #創建靜態框
        sb_button = wx.StaticBox(self.pnl, label="功能選項")
        #創建垂直box管理排版
        vsbox_button = wx.StaticBoxSizer(sb_button, wx.VERTICAL)
        #創建按鈕、綁定事件
        check_button = wx.Button(
            self.pnl, id=10, label="列出所有成員資訊", size=(150, 50))
        add_button = wx.Button(
            self.pnl, id=11, label="新增成員資料", size=(150, 50))
        delete_button = wx.Button(
            self.pnl, id=12, label="刪除成員資料", size=(150, 50))
        quit_button = wx.Button(
            self.pnl, id=13, label="離開", size=(150, 50))
        return_button =wx.Button(
            self.pnl,id=14, label ="返回登入",size=(150,50))
        #綁定id
        self.Bind(wx.EVT_BUTTON, self.ClickButton, id=10, id2=14)
        #新增按鈕到vsbox管理排版
        vsbox_button.Add(check_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(add_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(delete_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(quit_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(return_button, 0, wx.EXPAND | wx.BOTTOM, 40)        
        #創建靜態框
        sb_show_operation = wx.StaticBox(
            self.pnl, label="資訊顯示", size=(800, 500))
        #創建垂直box管理排版
        self.vsbox_show_operation = wx.StaticBoxSizer(
            sb_show_operation, wx.VERTICAL)
        #創建水平box管理排版
        hbox = wx.BoxSizer()
        hbox.Add(vsbox_button, 0, wx.EXPAND | wx.BOTTOM, 5)
        hbox.Add(self.vsbox_show_operation, 0, wx.EXPAND | wx.BOTTOM, 5)
        #將hbox新增到垂直box
        self.vbox.Add(hbox, proportion=0, flag=wx.CENTER)
        self.pnl.SetSizer(self.vbox)
    def ClickButton(self, event):
        source_id = event.GetId()
        if source_id == 10:
            #call InquireOp func
            inquire_button = InquireOp(
                None, title="hololive資料庫", size=(1024, 668))
            inquire_button.Show()
            self.Close(True)
        elif source_id == 11:
            #call AddOp func
            add_button = AddOp(None, title="hololive資料庫", size=(1024, 668))
            add_button.Show()
            self.Close(True)
        elif source_id == 12:
            #call DelOp func
            del_button = DelOp(None, title="hololive資料庫", size=(1024, 668))
            del_button.Show()
            self.Close(True)
        elif source_id == 13:
            self.Close(True)
        elif source_id == 14:
            #返回登入界面
            return_button = UserLogin(None, title="hololive資料庫", size=(1024, 668))
            return_button.Show()
            self.Close(True)

#繼承UserOperation類別，初始化操作界面
class InquireOp(UserOperation):
    def __init__(self, *args, **kw):
        #ensure the parent's __init__ is called
        super(InquireOp, self).__init__(*args, **kw)
        #創建表格
        self.holo_grid = self.CreateGrid()
        #新增到vsbox_show_operation管理排版
        self.vsbox_show_operation.Add(
            self.holo_grid, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 30)

    def ClickButton(self, event):
        source_id = event.GetId()
        if source_id == 10:
            #不用call自己
            pass
        elif source_id == 11:
            #call AddOp func
            add_button = AddOp(None, title="hololive資料庫", size=(1024, 668))
            add_button.Show()
            self.Close(True)
        elif source_id == 12:
            #call DelOp func
            del_button = DelOp(None, title="hololive資料庫", size=(1024, 668))
            del_button.Show()
            self.Close(True)
        elif source_id == 13:
            #結束
            self.Close(True)
        elif source_id == 14:
            #返回登入界面
            return_button = UserLogin(None, title="hololive資料庫", size=(1024, 668))
            return_button.Show()
            self.Close(True)

    def CreateGrid(self):
        #連接holo_db資料庫
        op = Sql_operation("holo_db")
        #獲得holo_info表中的資訊，回傳tuple
        np = op.FindAll("holo_info")
        column_names = ("ID","本名", "性别", "年齡", "身高", "別名", "所屬團體")
        holo_grid = wx.grid.Grid(self.pnl)
        holo_grid.CreateGrid(len(np), len(np[0]))
        #把資訊set到grid上
        for row in range(len(np)):
            holo_grid.SetRowLabelValue(row,str(row+1))
            for col in range(len(np[row])):
                holo_grid.SetColLabelValue(col, column_names[col])
                holo_grid.SetCellValue(row, col, str(np[row][col]))
        holo_grid.AutoSize()
        return holo_grid

#繼承UserOperation類別，初始化操作界面
class AddOp(UserOperation):
    def __init__(self, *args, **kw):
        #ensure the parent's __init__ is called
        super(AddOp, self).__init__(*args, **kw)
        #創建新增成員資料輸入框、新增按鈕
        self.holo_name = wx.TextCtrl(self.pnl, size=(210, 25))
        self.holo_gender = wx.TextCtrl(self.pnl, size=(210, 25))
        self.holo_age = wx.TextCtrl(self.pnl, size=(210, 25))
        self.holo_height = wx.TextCtrl(self.pnl, size=(210, 25))
        self.holo_alias = wx.TextCtrl(self.pnl, size=(210, 25))
        self.holo_group = wx.TextCtrl(self.pnl, size=(210, 25))
        self.add_affirm = wx.Button(self.pnl, label="新增", size=(80, 25))
        #為新增按鈕綁定事件
        self.add_affirm.Bind(wx.EVT_BUTTON, self.AddAffirm)
        #創建靜態框
        sb_name = wx.StaticBox(self.pnl, label="本名")
        sb_gender = wx.StaticBox(self.pnl, label="性别")
        sb_age = wx.StaticBox(self.pnl, label="年齡")
        sb_cid = wx.StaticBox(self.pnl, label="身高")
        sb_classid = wx.StaticBox(self.pnl, label="別名")
        sb_phone = wx.StaticBox(self.pnl, label="所屬團體")
        #創建水平box管理排版
        hsbox_name = wx.StaticBoxSizer(sb_name, wx.HORIZONTAL)
        hsbox_gender = wx.StaticBoxSizer(sb_gender, wx.HORIZONTAL)
        hsbox_age = wx.StaticBoxSizer(sb_age, wx.HORIZONTAL)
        hsbox_cid = wx.StaticBoxSizer(sb_cid, wx.HORIZONTAL)
        hsbox_classid = wx.StaticBoxSizer(sb_classid, wx.HORIZONTAL)
        hsbox_phone = wx.StaticBoxSizer(sb_phone, wx.HORIZONTAL)
        #新增到hsbox管理排版
        hsbox_name.Add(self.holo_name, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_gender.Add(self.holo_gender, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_age.Add(self.holo_age, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_cid.Add(self.holo_height, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_classid.Add(self.holo_alias, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_phone.Add(self.holo_group, 0, wx.EXPAND | wx.BOTTOM, 5)
        #新增到vsbox_show_operation管理排版
        self.vsbox_show_operation.Add(
            hsbox_name, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(
            hsbox_gender, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(
            hsbox_age, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(
            hsbox_cid, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(
            hsbox_classid, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(
            hsbox_phone, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(
            self.add_affirm, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)

    def ClickButton(self, event):
        source_id = event.GetId()
        if source_id == 10:
            #call InquireOp func
            inquire_button = InquireOp(
                None, title="hololive資料庫", size=(1024, 668))
            inquire_button.Show()
            self.Close(True)
        elif source_id == 11:
            #不用call自己
            pass
        elif source_id == 12:
            #call DelOp func
            del_button = DelOp(None, title="hololive資料庫", size=(1024, 668))
            del_button.Show()
            self.Close(True)
        elif source_id == 13:
            self.Close(True)
        elif source_id == 14:
            #返回登入界面
            return_button = UserLogin(None, title="hololive資料庫", size=(1024, 668))
            return_button.Show()
            self.Close(True)

    def AddAffirm(self, event):
        #連接holo_db資料庫
        op = Sql_operation("holo_db")
        #使用GetValue獲得輸入
        holo_name = self.holo_name.GetValue()
        holo_gender = self.holo_gender.GetValue()
        holo_age = self.holo_age.GetValue()
        holo_height = self.holo_height.GetValue()
        holo_alias = self.holo_alias.GetValue()
        holo_group = self.holo_group.GetValue()
        #向holo_info表新增成員資料
        np = op.Insert(holo_name, holo_gender, holo_age,
                       holo_height, holo_alias, holo_group)
        print("新增成功")

#繼承InquireOp類別，初始化操作界面
class DelOp(InquireOp):
    def __init__(self, *args, **kw):
        #ensure the parent's __init__ is called
        super(DelOp, self).__init__(*args, **kw)
        #創建刪除成員資訊輸入框、刪除按鈕
        self.del_id = wx.TextCtrl(self.pnl, pos=(407, 78), size=(210, 25))
        self.del_affirm = wx.Button(
            self.pnl, label="刪除", pos=(625, 78), size=(80, 25))
        #為刪除按鈕綁定事件
        self.del_affirm.Bind(wx.EVT_BUTTON, self.DelAffirm)
        #創建靜態框
        sb_del = wx.StaticBox(self.pnl, label="輸入需要刪除的成員ID")
        #創建水平box管理排版
        hsbox_del = wx.StaticBoxSizer(sb_del, wx.HORIZONTAL)
        #新增到hsbox_name管理排版
        hsbox_del.Add(self.del_id, 0, wx.EXPAND | wx.BOTTOM, 5)
        #新增到vsbox_show_operation管理排版
        self.vsbox_show_operation.Add(
            hsbox_del, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(
            self.del_affirm, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)

    def ClickButton(self, event):
        source_id = event.GetId()
        if source_id == 10:
            #call InquireOp func
            inquire_button = InquireOp(
                None, title="hololive資料庫", size=(1024, 668))
            inquire_button.Show()
            self.Close(True)
        elif source_id == 11:
            #call AddOp func
            add_button = AddOp(None, title="hololive資料庫", size=(1024, 668))
            add_button.Show()
            self.Close(True)
        elif source_id == 12:
            #不用call自己
            pass
        elif source_id == 13:
            self.Close(True)
        elif source_id == 14:
            #返回登入界面
            return_button = UserLogin(None, title="hololive資料庫", size=(1024, 668))
            return_button.Show()
            self.Close(True)
    def DelAffirm(self, event):
        #連接holo_db資料庫
        op = Sql_operation("holo_db")
        del_id = self.del_id.GetValue()
        print(del_id)
        #向holo_info表新增成員資料
        np = op.Del(int(del_id))
        #call自己
        print("刪除成功")
        del_button = DelOp(None, title="hololive資料庫", size=(1024, 668))
        del_button.Show()
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    login = UserLogin(None, title="hololive資料庫", size=(1024, 668))
    login.Show()
    app.MainLoop()