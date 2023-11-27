# Generated by Django 4.2.7 on 2023-11-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chitietdonhang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluong', models.SmallIntegerField(db_column='SoLuong')),
                ('dongia', models.IntegerField(db_column='DonGia')),
            ],
            options={
                'db_table': 'chitietdonhang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chitietgiay',
            fields=[
                ('idgiay', models.AutoField(db_column='IDGiay', db_comment='Mã của mặt hàng giầy', primary_key=True, serialize=False)),
                ('kichco', models.FloatField(db_column='KichCo')),
                ('mausac', models.CharField(db_column='MauSac', max_length=20)),
                ('sotonkho', models.IntegerField(db_column='SoTonKho')),
            ],
            options={
                'db_table': 'chitietgiay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChitiethoadonNhapHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluong', models.SmallIntegerField(db_column='SoLuong')),
                ('dongia', models.IntegerField(db_column='DonGia')),
            ],
            options={
                'db_table': 'chitiethoadon_nhap_hang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Danhmucgiay',
            fields=[
                ('iddanhmuc', models.AutoField(db_column='IDDanhMuc', primary_key=True, serialize=False)),
                ('tendanhmuc', models.CharField(db_column='TenDanhMuc', max_length=100)),
                ('loaigiay', models.CharField(db_column='LoaiGiay', max_length=50)),
                ('hangsanxuat', models.CharField(db_column='HangSanXuat', max_length=50)),
                ('giatien', models.IntegerField(db_column='GiaTien')),
                ('doituong', models.SmallIntegerField(db_column='DoiTuong', db_comment='Đối tượng hướng tới : Nam = 0,Nữ = 1, Khac = 2')),
            ],
            options={
                'db_table': 'danhmucgiay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Donhang',
            fields=[
                ('iddonhang', models.AutoField(db_column='IDDonHang', primary_key=True, serialize=False)),
                ('sotienthanhtoan', models.IntegerField(db_column='SoTienThanhToan')),
                ('createday', models.DateField(db_column='CreateDay')),
                ('createby', models.CharField(db_column='CreateBy', max_length=50)),
                ('trangthai', models.SmallIntegerField(db_column='TrangThai', db_comment='Trạng thái đon hàng : Checking=0, Confirm=1, Đang giao=2, Đã hoàn thành=3')),
                ('dvvanchuyen', models.CharField(blank=True, db_column='DVVanChuyen', max_length=100, null=True)),
                ('tennv_vanchuyen', models.CharField(blank=True, db_column='TenNV_VanChuyen', max_length=50, null=True)),
                ('sdt', models.CharField(blank=True, db_column='SDT', max_length=15, null=True)),
                ('socccd', models.CharField(blank=True, db_column='SoCCCD', max_length=20, null=True)),
                ('thoigiannhan', models.DateTimeField(blank=True, db_column='ThoiGianNhan', null=True)),
            ],
            options={
                'db_table': 'donhang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HoadonNhapHang',
            fields=[
                ('idhoadon', models.AutoField(db_column='IDHoaDon', primary_key=True, serialize=False)),
                ('sotienthanhtoan', models.IntegerField(db_column='SoTienThanhToan')),
                ('createday', models.DateField(db_column='CreateDay')),
                ('createby', models.CharField(db_column='CreateBy', max_length=50)),
            ],
            options={
                'db_table': 'hoadon_nhap_hang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Khachhang',
            fields=[
                ('idkhachhang', models.AutoField(db_column='IDKhachHang', primary_key=True, serialize=False)),
                ('tenkhachhang', models.CharField(db_column='TenKhachHang', max_length=50)),
                ('diachi', models.CharField(db_column='DiaChi', max_length=200)),
                ('email', models.CharField(db_column='Email', max_length=100)),
                ('sdt', models.CharField(db_collation='utf8mb3_general_ci', db_column='SDT', max_length=15)),
            ],
            options={
                'db_table': 'khachhang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviewsanpham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(db_column='Comment', max_length=300)),
            ],
            options={
                'db_table': 'reviewsanpham',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaikhoanKhachhang',
            fields=[
                ('idtaikhoan', models.AutoField(db_column='IDTaiKhoan', primary_key=True, serialize=False)),
                ('idkhachhang', models.CharField(db_column='IDKhachHang', max_length=255)),
                ('username', models.CharField(db_column='Username', max_length=30)),
                ('password', models.CharField(db_column='Password', max_length=30)),
                ('gioitinh', models.SmallIntegerField(db_column='GioiTinh', db_comment=' Nam = 0,Nữ = 1, Khac = 2')),
                ('ngaysinh', models.DateField(db_column='NgaySinh')),
                ('diemtichluy', models.IntegerField(db_column='DiemTichLuy')),
                ('ngaylaptk', models.DateField(db_column='NgayLapTK')),
            ],
            options={
                'db_table': 'taikhoan_khachhang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(db_column='IDUser', primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('tennhanvien', models.CharField(db_column='TenNhanVien', max_length=50)),
                ('tenchucvu', models.CharField(db_column='ChucVu', max_length=50)),
                ('gioitinh', models.SmallIntegerField(db_column='GioiTinh', db_comment=' Nam = 0,Nữ = 1, Khac = 2')),
                ('ngaysinh', models.DateField(db_column='NgaySinh')),
                ('date_joined', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_manager', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]